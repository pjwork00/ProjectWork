import { Component, OnInit } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';
import { Location } from '@angular/common';
import { HomePageInputForm } from 'src/app/models/homePageInputForm';
import { InputFormData } from 'src/app/serviceDataExchangeModels/inputFormData';
import { ApiService } from '../../api.service';
import { MapNameBuilder } from 'src/app/temporaryMapNameBuilder/MapNameBuilder';
import { Itinerary } from 'src/app/models/itinerary';

@Component({
  selector: 'app-itinerary-page',
  templateUrl: './itinerary-page.component.html',
  styleUrls: ['./itinerary-page.component.css']
})
export class ItineraryPageComponent implements OnInit {


  homePageInputForm: HomePageInputForm = new HomePageInputForm();
  itinerary : Itinerary = new Itinerary;

  constructor(public apiService: ApiService, public translate: TranslateService, private location: Location, inputFormData: InputFormData) {
    translate.addLangs(['en']);
    translate.setDefaultLang('en');
    // Initialization input form
    this.homePageInputForm = inputFormData.homePageInputForm;
  }

  switchLang(lang: string) {
    this.translate.use(lang);
  }

  ngOnInit(): void {

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
    this.itinerary.itineraries = mapNameBuilder.buildMapNames(this.homePageInputForm);
    this.itinerary.hotelsPath = mapNameBuilder.buildHotelNames(this.homePageInputForm);
    this.itinerary.restaurantsPath = mapNameBuilder.buildRestaurantNames(this.homePageInputForm);
  }

  setItinerary(itinerary: Itinerary) {
    this.itinerary = itinerary;
  }

}
