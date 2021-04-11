import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

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
    NearbyComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    TranslateModule.forRoot({
      loader: {
        provide: TranslateLoader,
        useFactory: httpTranslateLoader,
        deps: [HttpClient]
      }
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

// AOT compilation support
export function httpTranslateLoader(http: HttpClient) {
  return new TranslateHttpLoader(http);
}
