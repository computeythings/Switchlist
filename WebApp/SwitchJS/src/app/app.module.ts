import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { TableComponent } from './table/table.component';
import { SideMenuComponent } from './side-menu/side-menu.component';
import { RotateIconDirective } from './rotate-icon.directive';
import { TableEntryComponent } from './table-entry/table-entry.component';
import { NgbAccordionModule, NgbModalModule, NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CsvModalComponent } from './csv-modal/csv-modal.component';
import { SiteModalComponent } from './site-modal/site-modal.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { DiscoverModalComponent } from './discover-modal/discover-modal.component';
import { ScrapeModalComponent } from './scrape-modal/scrape-modal.component';
import { MatMenuModule } from '@angular/material/menu';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    TableComponent,
    SideMenuComponent,
    RotateIconDirective,
    CsvModalComponent,
    TableEntryComponent,
    SiteModalComponent,
    DiscoverModalComponent,
    ScrapeModalComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    NgbModule,
    NgbModalModule,
    NgbAccordionModule,
    FormsModule,
    HttpClientModule,
    MatMenuModule,
    MatButtonModule,
    MatIconModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
