import { Component } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';
import { SiteManagerService } from '../site-manager.service';

@Component({
  selector: 'app-scrape-modal',
  templateUrl: './scrape-modal.component.html',
  styleUrls: ['./scrape-modal.component.css'],
  host: {
    '(document:keydown)': 'onEnter($event)'
  }
})
export class ScrapeModalComponent {
  username = '';
  password = '';
  startUpdate: Function;
  constructor(public activeModal: NgbActiveModal) { }

  onEnter(event: any) {
    if (event.key === 'Enter') {
      this.submit()
    }
  }
  submit() {
    this.activeModal.dismiss();
    if ( this.startUpdate )
      this.startUpdate(this.username, this.password)
  }
}
