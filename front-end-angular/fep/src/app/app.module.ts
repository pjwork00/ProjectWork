import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatFormFieldModule} from '@angular/material/form-field';
import { MatNativeDateModule } from '@angular/material/core';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { InfoComponent } from './info/info.component';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { TranslateLoader, TranslateModule } from '@ngx-translate/core';
import { TranslateHttpLoader } from '@ngx-translate/http-loader';
import { ItinerarySearchSectionComponent } from './components/itinerary-search-section/itinerary-search-section.component';
import { FormsModule } from '@angular/forms';
import { ItineraryPageComponent } from './pages/itinerary-page/itinerary-page.component';
import { FooterComponent } from './components/footer/footer.component';
import { HeaderComponent } from './components/header/header.component';
import { RefreshItineraryComponent } from './components/refresh-itinerary/refresh-itinerary.component';
import { NearbyComponent } from './components/nearby/nearby.component';
import { DatepickerComponent } from './components/datepicker/datepicker.component';
import { MAT_DATE_FORMATS } from '@angular/material/core';



const MY_FORMATS = {
  parse: {
    dateInput: 'DD MMMM YYYY',
  },
  display: {
    dateInput: 'DD MMMM YYYY',
    monthYearLabel: 'MMMM YYYY',
    dateA11yLabel: 'LL',
    monthYearA11yLabel: 'MMMM YYYY',
  },
};



@NgModule({
  declarations: [
    AppComponent,
    InfoComponent,
    HomePageComponent,
    ItinerarySearchSectionComponent,
    ItineraryPageComponent,
    FooterComponent,
    HeaderComponent,
    RefreshItineraryComponent,
    NearbyComponent,
    DatepickerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    MatDatepickerModule,
    MatFormFieldModule,
    MatNativeDateModule,
    BrowserAnimationsModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: httpTranslateLoader,
        deps: [HttpClient]
      }
    })
  ],
  providers: [
    { provide: MAT_DATE_FORMATS, useValue: MY_FORMATS },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

// AOT compilation support
export function httpTranslateLoader(http: HttpClient) {
  return new TranslateHttpLoader(http);
}
