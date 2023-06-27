import { animate, state, style, transition, trigger } from '@angular/animations';
import { Component, Input, Output, ElementRef, EventEmitter } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Subscription } from 'rxjs';
import { SiteManagerService } from '../site-manager.service';
import { SiteModalComponent } from '../site-modal/site-modal.component';

@Component({
  selector: 'app-side-menu',
  templateUrl: './side-menu.component.html',
  styleUrls: ['./side-menu.component.css'],
  host: {
    '(document:click)': 'onClick($event)'
  },
  animations: [
    trigger('openClose', [
      state('expanded', style({
		    height: '*'
      })),
      state('collapsed', style({
		    height: '0'
      })),
      transition('expanded <=> collapsed', [
        animate('0.05s')
      ]),
    ]),
  ]
})
export class SideMenuComponent {
  @Input() isMenuOpen: boolean;
  @Output('toggleMenu') toggleMenu: EventEmitter<any> = new EventEmitter();
  
  sites: any = [];
  sitesExpanded = [];
  focusCategory: string = '';
  _siteSubscription: Subscription;
  constructor(private domRef: ElementRef, private modalService: NgbModal, private siteService: SiteManagerService) {
    siteService.getSites().subscribe(data => {
      this.sites = data
    })
    this._siteSubscription = siteService.siteChange.subscribe(newSites => {
      this.sites = newSites.sites;
    });
  }

  openSiteModal() {
    const modalRef = this.modalService.open(SiteModalComponent);
    this.menuToggle()
  }

  onClick(event: any) {
    if (this.isMenuOpen && event.target.id != 'menu-button') {
      if (!this.domRef.nativeElement.contains(event.target)) {
        this.menuToggle()
      }
    }
  }
  
  siteExpandToggle(siteIndex) {
    let i = this.sitesExpanded.indexOf(siteIndex)
    if ( i > -1 )
      return this.sitesExpanded.splice(i, 1);
    return this.sitesExpanded.push(siteIndex);
  }
  isSiteExpanded(siteIndex) {
    return this.sitesExpanded.includes(siteIndex);
  }

  menuSelect(category: string) {
    if ( this.focusCategory == category )
      this.focusCategory = '';
    else {
      this.focusCategory = category;
    }
    if (category != 'Sites') {
      alert('This page has not yet been implemented.')
      this.menuToggle();
    }
      
      
  }
  menuToggle() {
    this.toggleMenu.emit();
  }

  ngOnDestroy() {
    this._siteSubscription.unsubscribe();
  }
}
