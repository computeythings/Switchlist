import { Component, Input } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SiteManagerService } from '../site-manager.service';

@Component({
  selector: 'app-discover-modal',
  templateUrl: './discover-modal.component.html',
  styleUrls: ['./discover-modal.component.css'],
  host: {
    '(document:keydown)': 'onEnter($event)'
  }
})
export class DiscoverModalComponent {
  @Input() siteSubnets = {};
  @Input() sites: any = [];
  startJob: Function;
  username: string = '';
  password: string = '';
  scrape: boolean = false;
  constructor(public activeModal: NgbActiveModal, private siteService: SiteManagerService) { }

  onEnter(event: any) {
    if (event.key === 'Enter') {
      this.submit()
    }
  }

  sitesSelected() {
    return !Object.values(this.siteSubnets).includes(true)
  }

  submit() {
    let subnetsToScan = []
    for (let [subnet, scan] of Object.entries(this.siteSubnets)) {
      if ( scan ) {
        subnetsToScan.push(subnet)
      }
    }
    this.activeModal.dismiss();
    if ( subnetsToScan.length > 0 ) {
      this.siteService.discoverDevices(subnetsToScan, this.scrape, this.username, this.password);
      if ( this.startJob ) {
        this.startJob()
      }
    }
  }
}
