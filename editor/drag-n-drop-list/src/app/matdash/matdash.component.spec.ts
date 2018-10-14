
import { fakeAsync, ComponentFixture, TestBed } from '@angular/core/testing';

import { MatdashComponent } from './matdash.component';

describe('MatdashComponent', () => {
  let component: MatdashComponent;
  let fixture: ComponentFixture<MatdashComponent>;

  beforeEach(fakeAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ MatdashComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MatdashComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should compile', () => {
    expect(component).toBeTruthy();
  });
});
