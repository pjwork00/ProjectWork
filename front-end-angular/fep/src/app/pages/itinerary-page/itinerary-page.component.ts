import { Component, OnInit } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-itinerary-page',
  templateUrl: './itinerary-page.component.html',
  styleUrls: ['./itinerary-page.component.css']
})
export class ItineraryPageComponent implements OnInit {

  constructor(public translate: TranslateService) {
    translate.addLangs(['en']);
    translate.setDefaultLang('en');
   }

   switchLang(lang: string) {
    this.translate.use(lang);
  }

  ngOnInit(): void {
  }

}
