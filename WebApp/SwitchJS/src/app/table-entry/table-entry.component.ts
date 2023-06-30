import { Component, EventEmitter, Input, OnInit, Output, HostListener } from '@angular/core';
import { Subscription } from 'rxjs';
import { SiteManagerService } from '../site-manager.service';

@Component({
  selector: '[app-table-entry]',
  templateUrl: './table-entry.component.html',
  styleUrls: ['./table-entry.component.css']
})
export class TableEntryComponent implements OnInit {
  @Input() entry: any;
  @Input() index: string;
  @Input() tableHeaders: Array<{name:string, selector:string}>;
  @Input() filterString: string;
  @Output() tableCallback: EventEmitter<any> = new EventEmitter();
  icon: string = '';
  iconAlt: string = '';
  searchString: string = '';
  updatedString: string = '';
  selected: boolean = false;
  visible: boolean = false;
  detailView: boolean = false;
  scanning: boolean = false;
  neighborsCol1 = {};
  neighborsCol2 = null;
  ipCol1 = {};
  ipCol2 = null;
  vlansCol1 = {};
  vlansCol2 = null;
  _devicesChange: Subscription;

  statusIcons = {
    managed:{
      url:'assets/svg/good.svg',
      alt:'Online'
    },
    nologin:{
      url:'assets/svg/warning.svg',
      alt:'Unmanaged'
    },
    offline:{
      url:'assets/svg/error.svg',
      alt:'Offline'
    },
    scanning:{
      url:'assets/svg/scanning.svg',
      alt:'Scanning'
    }
  }

  SEARCHSKIP = [
    'managed',
    'reachable',
    'updated',
    'users',
    'uptime',
    'upstream'
  ]

  constructor(private siteService: SiteManagerService) { 
    this._devicesChange = siteService.devicesChange.subscribe(result => {
      if ( result.device === this.entry.scan_ip ) {
        if ( result.data ) {
          for ( let [key, value] of Object.entries(result.data) ) {
            this.entry[key] = value
          }
          this.updateVlans()
        }
        this.scanning = result.scanning;
      }
    });
  }

  ngOnInit(): void {
    this.updateNeighbors()
    this.updateIPs()
    this.selected = false
    this.visible = true
    this.setIcon()
    this.updateSearchString()

    this.tableCallback.emit({deviceCount: 1})
    this.tableCallback.emit({stackCount: this.entry.model.length})

    this.updatedString = new Date(this.entry.updated * 1000).toUTCString()
  }

  getTableValue(header) {
    switch(header) {
      case 'IP Address':
        return this.index;
      case 'Hostname':
        return this.entry.hostname || '<UNKNOWN>';
      case 'Model':
        return this.entry.base_model;
      case 'Firmware':
        return this.entry.firmware;
    }
    return '<UNKNOWN>'
  }

  isFiltered() {
    if (this.searchString.toUpperCase().includes(this.filterString.toUpperCase())) {
      this.toggleVisible(true);
      return true;
    }
    this.toggleSelect(false); // de-select when filtered out
    this.toggleDetailView(false); // hide detail view
    this.toggleVisible(false);
    return false;
  }

  setIcon() {
    let iconType = 'offline';
    if ( this.scanning ) {
      iconType = 'scanning'
    } 
    else if ( this.entry.managed ) {
      iconType = 'managed'
    }
    else if ( this.entry.reachable ) {
      iconType = 'nologin'
    }
    this.icon = this.statusIcons[iconType].url
    this.iconAlt = this.statusIcons[iconType].alt
    this.tableCallback.emit({})
  }

  portName(longform) {
    let shorthand = ''
    if ( this.entry.hasOwnProperty('make') ) {
      if ( this.entry.make === 'Cisco' ) 
        shorthand = longform.replace('AppGigabitEthernet', 'Ap').replace('FortyGigabitEthernet', 'Fo').replace('TwentyFiveGigE', 'Twe').replace('TenGigabitEthernet', 'Te').replace('GigabitEthernet', 'Gi').replace('FastEthernet', 'Fas').replace('Port-channel', 'Po')
      if ( this.entry.make === 'Brocade' )
        shorthand = `e${longform}`
    }
    return shorthand
  }

  updateSearchString() {
    // Setup entry-specific details
    let deviceSearchString = '';
    deviceSearchString+= this.entry.scan_ip;
    deviceSearchString+= this.entry.hostname;
    deviceSearchString+= this.entry.make;
    deviceSearchString+= this.entry.firmware;
    Object.keys(this.entry.ip_addresses).forEach(ip => {
      if ( ip == 'DHCP' )
        return
      deviceSearchString+= ip.split('/')[0];
      deviceSearchString+= this.entry.ip_addresses[ip]['interface']
    });
    this.entry.model.forEach(model => {
      deviceSearchString+= model
    });
    this.entry.serial.forEach(sn => {
      deviceSearchString+= sn
    });
    this.entry.base_mac.forEach(mac => {
      deviceSearchString+= mac
    });
    
    this.searchString = deviceSearchString;
  }
  updateNeighbors() {
    let neighborCount = Object.keys(this.entry.neighbors).length;
    if ( neighborCount > 25) {
      this.neighborsCol2 = {};
      let cutoff = Math.ceil(neighborCount/2);
      let index = 0;
      for ( let [key, value] of Object.entries(this.entry.neighbors )) {
        if ( index < cutoff )
          this.neighborsCol1[key] = value;
        else
          this.neighborsCol2[key] = value;
        index++;
      }
    }
    else
      this.neighborsCol1 = this.entry.neighbors;
  }
  updateIPs() {
    let ipCount = Object.keys(this.entry.ip_addresses).length;
    if ( ipCount > 25) {
      this.ipCol2 = {};
      let cutoff = Math.ceil(ipCount/2);
      let index = 0;
      for ( let [key, value] of Object.entries(this.entry.ip_addresses )) {
        if ( index < cutoff )
          this.ipCol1[key] = value;
        else
          this.ipCol2[key] = value;
        index++;
      }
    }
    else
      this.ipCol1 = this.entry.ip_addresses;
  }

  updateVlans() {
    let vlanCount = Object.keys(this.entry.vlans).length;
    if ( vlanCount > 25 ) {
      this.vlansCol2 = {};
      let cutoff = Math.ceil(vlanCount/2)
      let index = 0;
      for ( let [key, value] of Object.entries(this.entry.neighbors)) {
        if ( index < cutoff ) 
          this.vlansCol1[key] = value;
        else
          this.vlansCol2[key] = value;
        index++;
      }
    }
    else 
      this.vlansCol1 = this.entry.vlans;
  }

  toggleVisible(visible: boolean) {
    this.visible = visible
  }

  toggleSelect(selected: boolean) {
    if (this.selected != selected) {
      if (selected)
        this.tableCallback.emit({selectedCount: 1})
      else
        this.tableCallback.emit({selectedCount: -1})
    }
    this.selected = selected
  }

  detailViewUpdate() {
    this.tableCallback.emit({ viewDetail: this.index })
  }

  toggleDetailView(show = false) {
    this.detailView = show
    if ( this.detailView ) {
      this.tableCallback.emit({ viewDetail: this.index })
    }
  }

  getView() {
    return this.detailView ? 'expanded' : 'collapsed';
  }

  ngOnDestroy() {
    this._devicesChange.unsubscribe();
  }
}
