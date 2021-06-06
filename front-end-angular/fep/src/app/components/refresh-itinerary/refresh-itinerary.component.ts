import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { HomePageInputForm } from 'src/app/models/homePageInputForm';
import { Router } from '@angular/router';
import { ApiService } from '../../api.service';
import { Book } from 'src/app/models/book';
import { MapNameBuilder } from 'src/app/temporaryMapNameBuilder/MapNameBuilder';

@Component({
  selector: 'app-refresh-itinerary',
  templateUrl: './refresh-itinerary.component.html',
  styleUrls: ['./refresh-itinerary.component.css']
})
export class RefreshItineraryComponent implements OnInit {

  constructor(public apiService : ApiService, private readonly router: Router) { }

  ngOnInit(): void {

    // Forced book - to be deleted
    this.homePageInputForm.selectedBook = this.booksList[0];
  }

  @Input() homePageInputForm : HomePageInputForm = new HomePageInputForm;
  itinerary? : String[];
  @Output() itineraryChange: EventEmitter<String[]> = new EventEmitter();
 
   booksList: Book[] = [{ title: 'Angels & Demons' },
  //  { title: 'Inferno' },
  //  { title: 'Origin' },
   { title: 'Da Vinci Code' },
  //  { title: 'The Alchemist' },
  //  { title: 'Hornet Flight' },
  //  { title: 'Jackdaws' }
   ];
  
   setStartDate(input: Date) {
     this.homePageInputForm.startDate = input;
   }
 
   setEndDate(input: Date) {
     this.homePageInputForm.endDate = input;
   }
 
   setCulture(input: any) {
     this.homePageInputForm.culture = input;
   }
 
   setNature(input: any) {
     this.homePageInputForm.nature = input;
   }
 
   setRecreation(input: any) {
     this.homePageInputForm.recreation = input;
   }
 
   setSpeed(input: any) {
     this.homePageInputForm.speed = input;
   }
 
   setBudget(input: any) {
     this.homePageInputForm.budget = input;
   }

   submitHomePageInput(){
    /* Temprorary disabled 
     this.apiService.getItinerary(this.homePageInputForm).subscribe((data)=>{
      if (data != null) {
        this.itinerary = data.result;
        this.itineraryChange.emit(this.itinerary);
        console.log("Itinerary section : getItinerary responds correctly");
      }
    }); */

    // Temporary itinerary builder
    var mapNameBuilder : MapNameBuilder = new MapNameBuilder();
    this.itinerary = mapNameBuilder.buildMapNames(this.homePageInputForm);
    this.itineraryChange.emit(this.itinerary);
  }

}
