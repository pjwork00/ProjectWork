import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ItinerarySearchSectionComponent } from './itinerary-search-section.component';

describe('ItinerarySearchSectionComponent', () => {
  let component: ItinerarySearchSectionComponent;
  let fixture: ComponentFixture<ItinerarySearchSectionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ItinerarySearchSectionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ItinerarySearchSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
