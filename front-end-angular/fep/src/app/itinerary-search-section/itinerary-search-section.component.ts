import { Component, Input, OnInit } from '@angular/core';
import { NgForm} from '@angular/forms';
import { ApiService } from '../api.service';
import { Book } from '../models/book';
import { HomePageInputForm } from '../models/homePageInputForm';

@Component({
  selector: 'app-itinerary-search-section',
  templateUrl: './itinerary-search-section.component.html',
  styleUrls: ['./itinerary-search-section.component.css']
})
export class ItinerarySearchSectionComponent implements OnInit {


  @Input() homePageInputForm : HomePageInputForm = new HomePageInputForm;

  booksList : Book[] = [{title : 'Angels & Demons'}, {title : 'The Great Gatsby'}, {title : 'The Odyssey'}];

  constructor(public apiService : ApiService){
    this.homePageInputForm.selectedBook = "Select a book"
  }

  
  ngOnInit(): void {
  }


  setSelectedBook(s : String){
    this.homePageInputForm.selectedBook = s;
  }

  submitHomePageInput(){
    this.apiService.getItinerary(this.homePageInputForm).subscribe((data)=>{
      if(data != null){
        console.log("Itinerary section : getItinerary responds correctly");
      }
    });
  }

}
