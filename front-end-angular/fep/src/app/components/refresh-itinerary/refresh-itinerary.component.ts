import { Component, Input, OnInit } from '@angular/core';
import { HomePageInputForm } from 'src/app/models/homePageInputForm';
import { Router } from '@angular/router';
import { ApiService } from '../../api.service';
import { Book } from 'src/app/models/book';

@Component({
  selector: 'app-refresh-itinerary',
  templateUrl: './refresh-itinerary.component.html',
  styleUrls: ['./refresh-itinerary.component.css']
})
export class RefreshItineraryComponent implements OnInit {

  constructor(public apiService : ApiService, private readonly router: Router) { }

  ngOnInit(): void {
  }

  @Input() homePageInputForm : HomePageInputForm = new HomePageInputForm;
 
   booksList: Book[] = [{ title: 'Angels & Demons' },
   { title: 'Inferno' },
   { title: 'Origin' },
   { title: 'Da Vinci Code' },
   { title: 'The Alchemist' },
   { title: 'Hornet Flight' },
   { title: 'Jackdaws' }
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
    this.apiService.getItinerary(this.homePageInputForm).subscribe((data)=>{
      if(data != null){
        console.log("Itinerary section : getItinerary responds correctly");
      }
    });
  }

}
