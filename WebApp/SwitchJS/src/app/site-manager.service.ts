import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { HttpClient, HttpResponse } from '@angular/common/http';
const OPTIONS = {headers: {'Content-Type': 'application/json'}}

@Injectable({
  providedIn: 'root'
})
export class SiteManagerService {
  private server: string = 'http://localhost:5000';
  private currentJob = null;
  private lastEvent = '';
  private serverUpdates: EventSource;
  public siteChange: Subject<any> = new Subject<any>();
  public jobChange: Subject<any> = new Subject<any>();
  public devicesChange: Subject<any> = new Subject<any>();

  constructor(private http: HttpClient) {
  }

  openStream() {
    console.log('Opening IO Stream...')
    let eventQuery = `?event-id=${this.lastEvent}`
    this.serverUpdates = new EventSource(`${this.server}/iostream${eventQuery}`);
    this.serverUpdates.onmessage = (event) => {
      let data = JSON.parse(event.data)
      console.log('Event Sourced')
      console.log(data)
      switch( data.type ) {
        case 'device_update':
          this.devicesChange.next({ action: 'update', device: data.ip, data: data.attributes, scanning: data.scanning })
          break;
        case 'site_update':
          this.siteChange.next({ action: 'update', sites: data.sites })
          break;
        case 'job_update':
          if ( data.job.status === 'completed' || data.job.status === 'cancelled')
            this.currentJob = null
          else
            this.currentJob = data.job
          this.jobChange.next({ running: this.isScanning(), progress: this.jobProgress() })
          break;
        default:
          console.log(`Unhandled event_type: ${data}`)
          console.log(data)
      }
      this.lastEvent = data.eventId
    }
    this.serverUpdates.onerror = (error) => {
      console.log('SSE Error:')
      console.error(error)
    }
  }

  jobProgress() {
    if ( this.currentJob === null )
      return 0
    return ( this.currentJob.completed.length / this.currentJob.size ) * 100
  }
  isScanning() {
    return this.currentJob !== null;
  }
  getTableData() {
    let tableDataURL = '/api/v1/devices'
    return this.http.get(this.server + tableDataURL)
  }
  getSites() {
    let sitesURL = '/api/v1/sites'
    return this.http.get(this.server + sitesURL)
  }
  setSites(siteInfo) {
    let sitesURL = '/api/v1/sites'
    return this.http.post<HttpResponse<any>>(this.server + sitesURL, JSON.stringify({sites: siteInfo}), { observe: 'response' }).subscribe(response => {
      console.log(response)
    })
  }
  discoverDevices(addresses=[], scrape=false, username='', password='') {
    let discoveryURL = '/api/v1/discover'
    let data =  {
        addresses: addresses,
        scrape: scrape,
        username: username,
        password: password
    }
    this.http.post(this.server + discoveryURL, JSON.stringify(data), { observe: 'response' }).subscribe({
      next: response => {
        if ( response.status != 201)
          return this.jobChange.next({ running: false, progress: 0 })
        this.currentJob = response.body
      },
      error: error => {
        console.error(error)
        return this.jobChange.next({ running: false, progress: 0 })
      }})
  }
  updateDevices(ipList, username='', password='') {
    let scrapeURL = '/api/v1/scrape'
    return this.http.post(this.server + scrapeURL, JSON.stringify({addresses: ipList, username: username, password: password}), OPTIONS).subscribe(data => {
        console.log(data)
    })
  }
  deleteDevices(ipList, username='', password='') {
    let tableDataURL = '/api/v1/devices'
    return this.http.post(this.server + tableDataURL, JSON.stringify({method: 'DELETE', ipList: ipList, username: username, password: password}), OPTIONS)
  }
  updateSecureCRTLocal(switchList) {
    let crtURL = '/api/v1/crtupdate'
    return this.http.post(this.server + crtURL, JSON.stringify(switchList), OPTIONS).subscribe(data => {
        console.log(data);
    })
  }
}
