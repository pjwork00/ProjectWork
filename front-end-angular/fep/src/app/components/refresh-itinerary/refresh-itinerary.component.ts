import { Component, Input, OnInit } from '@angular/core';
import { HomePageInputForm } from 'src/app/models/homePageInputForm';
import { Router } from '@angular/router';
import { ApiService } from '../../api.service';

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

  setSelectedBook(s : String){
    this.homePageInputForm.selectedBook.title = s;
  }

  submitHomePageInput(){
    this.apiService.getItinerary(this.homePageInputForm).subscribe((data)=>{
      if(data != null){
        console.log("Itinerary section : getItinerary responds correctly");
      }
    });
  }

}
