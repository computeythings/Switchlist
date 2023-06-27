import { Component, Input } from '@angular/core';
import { SiteManagerService } from '../site-manager.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  constructor(private siteService: SiteManagerService) {
  }
  isMenuOpen = false;
  toggleMenu() {
    this.isMenuOpen = !this.isMenuOpen;
  }
  onOptionClick(option: string) {
    if ( option === 'UpdateCRT' ) {
      console.log('UpdateCRT button clicked')
      this.siteService.updateSecureCRTLocal({})
    }
    if ( option === 'Settings' ) {
      alert('TODO: IMPLEMENT SETTINGS FUNCTION')
    }
  }
}
