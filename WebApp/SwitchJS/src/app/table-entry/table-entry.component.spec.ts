import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TableEntryComponent } from './table-entry.component';

describe('TableEntryComponent', () => {
  let component: TableEntryComponent;
  let fixture: ComponentFixture<TableEntryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TableEntryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TableEntryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
