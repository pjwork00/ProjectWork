import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { InputFormData } from 'src/app/serviceDataExchangeModels/inputFormData';
import { Book } from '../../models/book';
import { HomePageInputForm } from '../../models/homePageInputForm';


@Component({
  selector: 'app-itinerary-search-section',
  templateUrl: './itinerary-search-section.component.html',
  styleUrls: ['./itinerary-search-section.component.css'],
})
export class ItinerarySearchSectionComponent implements OnInit {

  // Variables
  homePageInputForm: HomePageInputForm;
  inputFormDataLocal: InputFormData;

  booksList: Book[] = [{ title: 'Angels & Demons' },
  { title: 'Inferno' },
  { title: 'Origin' },
  { title: 'Da Vinci Code' },
  { title: 'The Alchemist' },
  { title: 'Hornet Flight' },
  { title: 'Jackdaws' }
  ];

  constructor(private readonly router: Router, inputFormData: InputFormData) {
    var defaultBook: Book = { title: "Select a book" };
    this.homePageInputForm = new HomePageInputForm;
    this.homePageInputForm.selectedBook = defaultBook;
    this.inputFormDataLocal = inputFormData;
  }


  ngOnInit(): void {
  }

  ngOnDestroy(): void {
    this.inputFormDataLocal.homePageInputForm = this.homePageInputForm;
  }

  submitHomePageInput() {
    // Go to itinerary page by route 
    this.router.navigate(['itineraryPage']);
  }

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

}
