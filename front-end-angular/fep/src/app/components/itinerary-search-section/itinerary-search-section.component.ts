import { Component, Input, OnInit } from '@angular/core';
import { NgForm} from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../../api.service';
import { Book } from '../../models/book';
import { HomePageInputForm } from '../../models/homePageInputForm';


@Component({
  selector: 'app-itinerary-search-section',
  templateUrl: './itinerary-search-section.component.html',
  styleUrls: ['./itinerary-search-section.component.css']
})
export class ItinerarySearchSectionComponent implements OnInit {


  homePageInputForm : HomePageInputForm;

  booksList : Book[] = [{title : 'Angels & Demons'}, 
  {title : 'Inferno'}, 
  {title : 'Origin'},
  {title : 'Da Vinci Code'},
  {title : 'The Alchemist'},
  {title : 'Hornet Flight'},
  {title : 'Jackdaws'}
];

  constructor(public apiService : ApiService, private readonly router: Router){
    var defaultBook : Book = {title: "Select a book"};
    this.homePageInputForm = new HomePageInputForm;
    this.homePageInputForm.selectedBook = defaultBook;
  }

  
  ngOnInit(): void {
  }

  submitHomePageInput(){
    this.apiService.getItinerary(this.homePageInputForm).subscribe((data)=>{
      if(data != null){
        console.log("Itinerary section : getItinerary responds correctly");
      }
    });
    
    // Go to itinerary page by route 
    //this.router.navigate(['itineraryPage']);
  }

  setStartDate(input: Date){
    this.homePageInputForm.startDate = input;
  }

  setEndDate(input: Date){
    this.homePageInputForm.endDate = input;
  }

  setCulture(input: any){
    this.homePageInputForm.culture = input;
  }

  setNature(input: any){
    this.homePageInputForm.nature = input;
  }

  setRecreation(input: any){
    this.homePageInputForm.recreation = input;
  }

  setSpeed(input: any){
    this.homePageInputForm.speed = input;
  }

  setBudget(input: any){
    this.homePageInputForm.budget = input;
  }

}
