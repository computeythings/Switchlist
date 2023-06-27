import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DiscoverModalComponent } from './discover-modal.component';

describe('DiscoverModalComponent', () => {
  let component: DiscoverModalComponent;
  let fixture: ComponentFixture<DiscoverModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DiscoverModalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DiscoverModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
