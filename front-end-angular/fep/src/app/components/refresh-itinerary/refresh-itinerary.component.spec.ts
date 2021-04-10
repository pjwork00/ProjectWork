import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RefreshItineraryComponent } from './refresh-itinerary.component';

describe('RefreshItineraryComponent', () => {
  let component: RefreshItineraryComponent;
  let fixture: ComponentFixture<RefreshItineraryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RefreshItineraryComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RefreshItineraryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
