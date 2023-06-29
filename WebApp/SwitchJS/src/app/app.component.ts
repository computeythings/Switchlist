import { Component } from '@angular/core';
import { SiteManagerService } from './site-manager.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'SwitchJS';

  constructor(private siteService: SiteManagerService) { 
    this.siteService.openStream()
  }
}
