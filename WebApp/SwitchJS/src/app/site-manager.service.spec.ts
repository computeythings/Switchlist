import { TestBed } from '@angular/core/testing';

import { SiteManagerService } from './site-manager.service';

describe('SiteManagerService', () => {
  let service: SiteManagerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SiteManagerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
