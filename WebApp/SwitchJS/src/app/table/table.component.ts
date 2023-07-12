import { Input, Component, ChangeDetectorRef, ViewChildren, QueryList, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CsvModalComponent } from '../csv-modal/csv-modal.component';
import { DiscoverModalComponent } from '../discover-modal/discover-modal.component';
import { ScrapeModalComponent } from '../scrape-modal/scrape-modal.component';
import { SiteManagerService } from '../site-manager.service';
import { Subject, debounceTime } from 'rxjs';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['../app.component.css', './table.component.css']
})
export class TableComponent implements OnInit {
  @ViewChildren('tableRow') tableRows: QueryList<any>;
  tableData: any = [];
  detailChildIndex = -1;
  filterString: string = '';
  readonly SORT_ASC = 'asc';
  readonly SORT_DESC = 'desc';
  _discoverSubscription;
  _deviceSubscription;
  sortKey = 'scan_ip';
  sortOrder = this.SORT_ASC;
  jobRunning = false;
  allSelected = false;
  stackCount = 0;
  deviceCount = 0;
  selectedCount = 0;
  discoverProgress = 0;
  updateFilter$ = new Subject<string>();
  tableHeaders: Array<{name:string, selector:string}>= [
    {name: 'Hostname', selector: 'hostname'},
    {name: 'IP Address', selector: 'scan_ip'},
    {name: 'Model', selector: 'base_model'},
    {name: 'Firmware', selector: 'firmware'},
    {name: 'Status', selector: 'status'}
  ]
  columnFilters: { [key:string]: string } = {
    hostname: '',
    scan_ip: '',
    base_model: '',
    firmware: '',
    status: ''
  };

  constructor(private cdr: ChangeDetectorRef, private modalService: NgbModal, private siteService: SiteManagerService) {
    this.updateFilter$.pipe(debounceTime(300)).subscribe((value) => {
      this.filterString = value
      this.cdr.detectChanges()
    });
    this._discoverSubscription = siteService.jobChange.subscribe(result => {
      this.jobRunning = result.running;
      this.discoverProgress = result.progress;
      this.cdr.detectChanges()
    });
    this._deviceSubscription = siteService.devicesChange.subscribe(update => {
      let entryExists = this.tableRows.find((rowElement: any, index: number, unkArray: any[]) => {
        return rowElement.entry.scan_ip === update.device;
      });
      if ( 'reachable' in update.data && update.data.reachable) {
        if ( !entryExists ) {
          this.tableData.push({
            "scan_ip": update.device,
            "base_subnet": "",
            "hostname": "",
            "ip_addresses": {},
            "make": "",
            "model": [],
            "base_model": "",
            "firmware": "",
            "serial": [],
            "upstream": "",
            "fips": false,
            "neighbors": {},
            "updated": Date.now()/1000, // Normalize for server-side date format
            "uptime": 0,
            "users": 0,
            "base_mac": [],
            "managed": false,
            "reachable": true,
            "configs": {}
          })
        }
      }
      if ( 'scanning' in update) {
        entryExists.scanning = update.scanning
      }
      if (this.sortOrder == this.SORT_ASC)
        this.sortAscending(this.tableData, this.sortKey) 
      else
        this.sortDescending(this.tableData, this.sortKey)
      this.cdr.detectChanges()
    })
  }
  ngOnInit(): void {
    this.tableUpdate();
  }

  countDevices() {
    let count = 0;
    let lastDevice = null;
    if (this.tableRows) {
      this.tableRows.forEach(device => {
        if ( !device.visible )
          return
        lastDevice = device;
        count++;
      });
    }
    if ( count === 1 ) {
      // if there's only one device, expand detail view (do not propagate update as this will cause a loop)
      lastDevice.toggleDetailView(true, true);
    }
    return count
  }
  countStackMembers() {
    let count = 0;
    if (this.tableRows) {
      this.tableRows.forEach(device => {
        if ( !device.visible )
          return
        if (device.entry.managed)
          count+= device.entry.model.length;
        else
          count++;
      });
    }
    return count
  }
  tableUpdate() {
    this.tableData = []
    this.siteService.getTableData().subscribe(data => {
      let dataHolder: any = data;
      dataHolder.forEach(ip => {
        if (ip.managed || ip.reachable)
          this.tableData.push(ip)
      })
      this.sortAscending(this.tableData, this.sortKey)
    });
  }

  /*
    callback for when the top thead checkbox is clicked
     - either checks all boxes or if they are all checked, unchecks all
  */
  toggleSelectAll(checked: boolean) {
    this.allSelected = checked;
    this.selectedCount = 0; // reset selected count
    this.tableRows.forEach(device => {
      if (device.visible) {
        device.selected = this.allSelected
        if (device.selected)
          this.selectedCount+= 1
      }
    });
    this.cdr.detectChanges()
  }
  updateColFilter(event, columnName) {
    this.columnFilters[columnName] = event.target.value
    this.cdr.detectChanges()
  }
  /*
    callback used by table-entry child components to update parent data
  */
    tableEntryCallback(data) {
      if ('selectedCount' in data) {
        this.selectedCount += data.selectedCount;
      }
      if ('deviceCount' in data) {
        this.deviceCount += data.deviceCount;
      }
      if ('stackCount' in data) {
        this.stackCount += data.stackCount;
      }
      
      // Manually trigger change detection to update the UI
      this.cdr.detectChanges();
    }

  /* 
    each header field has sort buttons that call this sort function to sort by the 
    field key and alternate between ascending and descending order
  */
  tableSort(key: string, force: boolean = false) {
    // toggle sort order if the same key is clicked twice
    if (key == this.sortKey) {
      if (this.sortOrder == this.SORT_ASC) {
        this.sortOrder = this.SORT_DESC
      } else {
        this.sortOrder = this.SORT_ASC
      }
    } else {
      // set sort key and default to ascending order
      this.sortKey = key;
      this.sortOrder = this.SORT_ASC
    }
    
    if (this.sortOrder == this.SORT_ASC) {
      var list = this.sortAscending(this.tableData, key)
    } else {
      var list = this.sortDescending(this.tableData, key)
    }
    return list;
  }
  sortAscending(list, key) {
    return list.sort((a, b) => {
      var x = a[key]; var y = b[key];
      
      if ( key === 'scan_ip' ) { 
        let xOctets = x.split('.').map(Number);
        let yOctets = y.split('.').map(Number);
        for ( let i = 0; i < xOctets.length; i++) {
          let octectCompare = ((xOctets[i] < yOctets[i]) ? -1 : ((xOctets[i] > yOctets[i]) ? 1 : 0))
          if ( octectCompare != 0 ) {
            return octectCompare
          }
        }
      }
      if ( key === 'status' ) {
        let managedX = a['managed']
        let reachableX = a['reachable']
        x = (managedX + reachableX) * reachableX
        let managedY = b['managed']
        let reachableY = b['reachable']
        y = (managedY + reachableY) * reachableY
      }

      return ((x < y) ? -1 : ((x > y) ? 1 : 0));
    });
  }
  sortDescending(list, key) {
    return list.sort((a, b) => {
      var x = a[key]; var y = b[key];

      if ( key === 'scan_ip' ) { 
        let xOctets = x.split('.').map(Number);
        let yOctets = y.split('.').map(Number);
        for ( let i = 0; i < xOctets.length; i++) {
          let octectCompare = ((xOctets[i] < yOctets[i]) ? 1 : ((xOctets[i] > yOctets[i]) ? -1 : 0))
          if ( octectCompare != 0 ) {
            return octectCompare
          }
        }
      }
      if ( key === 'status' ) {
        let managedX = a['managed']
        let reachableX = a['reachable']
        x = (managedX + reachableX) * reachableX
        let managedY = b['managed']
        let reachableY = b['reachable']
        y = (managedY + reachableY) * reachableY
      }

      return ((x < y) ? 1 : ((x > y) ? -1 : 0));
    });
  }

  discover() {
    // Pull site info and open modal
    this.siteService.getSites().subscribe(data => {
      let siteSubnets = {};
      let sites: any = data;
      for (let site of sites )
        for (let subnet of site.subnets)
          siteSubnets[subnet] = true;

      const modalRef = this.modalService.open(DiscoverModalComponent);
      modalRef.componentInstance.sites = sites;
      modalRef.componentInstance.siteSubnets = siteSubnets;
      modalRef.componentInstance.startJob = () => { this.jobRunning = true; };
    });
  }

  deleteDevices() {
    // delete selected devices
    if ( !confirm(`Delete ${this.selectedCount} devices?`) )
      return
    let deleteDevices = [];
    let deleteIndexes = [];
    this.tableRows.forEach((device, index) => {
      if ( device.selected ) {
        deleteDevices.push(device.entry.scan_ip);
        deleteIndexes.push(index);
      }
    });
    this.siteService.deleteDevices(deleteDevices).subscribe({
      next: data =>  {
        deleteIndexes.forEach((devIndex, offset) => {
          this.tableData.splice(devIndex - offset, 1);
          this.selectedCount--;
        });
      },
      error: err =>  {
        console.error(err)
      }
    })
  }

  /*
    EXPORT FILE FUNCTIONS
  */
  saveCSVDialog() {
    let saveDevices = []
    this.tableRows.forEach(device => {
      if ( device.selected || this.selectedCount === 0 ) {
        saveDevices.push(device.entry);
      }
    });
    const modalRef = this.modalService.open(CsvModalComponent);
    modalRef.componentInstance.devices = saveDevices
  }

  /*
    DEVICE MANAGEMENT FUNCTIONS:
  */
 updateDevices() {
  if (this.selectedCount == 0)
    return; // avoid creating an empty job or running multiple jobs simultaneously
  let scanJob = []
  this.tableRows.forEach(device => {
    if ( device.selected )
      scanJob.push(device.entry['scan_ip'])
  });
  const modalRef = this.modalService.open(ScrapeModalComponent);
  modalRef.componentInstance.startUpdate = (username, password) => { 
    this.toggleSelectAll(false); 
    this.siteService.updateDevices(scanJob, username, password);
  }
 }

 ngOnDestroy() {
  this._discoverSubscription.unsubscribe();
 }
}
