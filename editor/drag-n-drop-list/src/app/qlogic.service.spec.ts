import { TestBed } from '@angular/core/testing';

import { QLogicService } from './qlogic.service';

describe('QLogicService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: QLogicService = TestBed.get(QLogicService);
    expect(service).toBeTruthy();
  });
});
