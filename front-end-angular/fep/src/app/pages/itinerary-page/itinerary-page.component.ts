import { Component, OnInit } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';
import { Location } from '@angular/common';
import { HomePageInputForm } from 'src/app/models/homePageInputForm';
import { InputFormData } from 'src/app/serviceDataExchangeModels/inputFormData';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-itinerary-page',
  templateUrl: './itinerary-page.component.html',
  styleUrls: ['./itinerary-page.component.css']
})
export class ItineraryPageComponent implements OnInit {


  homePageInputForm: HomePageInputForm = new HomePageInputForm();

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
    this.apiService.getItinerary(this.homePageInputForm).subscribe((data) => {
      if (data != null) {
        console.log("Itinerary section : getItinerary responds correctly");
      }
    });
  }

}
