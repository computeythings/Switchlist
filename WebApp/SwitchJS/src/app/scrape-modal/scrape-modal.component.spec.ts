import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ScrapeModalComponent } from './scrape-modal.component';

describe('ScrapeModalComponent', () => {
  let component: ScrapeModalComponent;
  let fixture: ComponentFixture<ScrapeModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ScrapeModalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ScrapeModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
