import { Component, OnInit } from '@angular/core';
import { Book } from '../models/book';
import { HomePageInputForm } from '../models/homePageInputForm';

@Component({
  selector: 'app-itinerary-search-section',
  templateUrl: './itinerary-search-section.component.html',
  styleUrls: ['./itinerary-search-section.component.css']
})
export class ItinerarySearchSectionComponent implements OnInit {


  homePageInputForm : HomePageInputForm;

  booksList : Book[] = [{title : 'Angels & Demons'}, {title : 'The Great Gatsby'}, {title : 'The Odyssey'}];

  constructor(){
    this.homePageInputForm = new HomePageInputForm();
    this.homePageInputForm.selectedBook = "Select a book"
  }

  
  ngOnInit(): void {
  }


  setSelectedBook(s : String){
    this.homePageInputForm.selectedBook = s;
  }

}
