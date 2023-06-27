import { Component, OnInit } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SiteManagerService } from '../site-manager.service';

@Component({
  selector: 'app-site-modal',
  templateUrl: './site-modal.component.html',
  styleUrls: ['./site-modal.component.css'],
  host: {
    '(document:keydown)': 'onEnter($event)'
  }
})

export class SiteModalComponent implements OnInit {
  sites: any = [];
  scanNow: boolean = false;
  siteFocus: number = -1;
  newIndeces = [];

  constructor(public activeModal: NgbActiveModal, private siteService: SiteManagerService) {
    siteService.getSites().subscribe(data => {
      this.sites = data
    })
  }
  onEnter(event: any) {
    if (event.key === 'Enter') {
      this.submit()
    }
  }
  ngOnInit(): void {
    this.sites = JSON.parse(JSON.stringify(this.sites));
  }

  subnetIndexTracker(index: any, item: any) {
    return index;
  }
  nameIndexTracker(index: any, item: any) {
    return index;
  }

  addSubnet(siteIndex) {
    this.sites[siteIndex].subnets.push('');
  }
  removeSubnet(siteIndex, subnetIndex) {
    this.sites[siteIndex].subnets.splice(subnetIndex, 1)
  }
  addSite() {
    this.sites.push({
      name: '',
      subnets: ['']
    })
  }
  removeSite(index) {
    this.sites.splice(index, 1)
  }
  submit() {
    this.siteService.setSites(this.sites);
    this.activeModal.close()
  }
}
