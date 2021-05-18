import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HomePageInputForm } from './models/homePageInputForm';
import { ItineraryOutput } from './serviceModels/ItineraryOutput';
import {formatDate} from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) { }


  public getInfo(): Observable<ItineraryOutput> {
    return this.httpClient.get<ItineraryOutput>(`http://127.0.0.1:8081/`, { responseType: 'json' });
  }



  public getItinerary(input: HomePageInputForm): Observable<ItineraryOutput> {

    var startDate =formatDate(input.startDate, 'yyyy-MM-dd', "en-US");
    var endDate = formatDate(input.endDate, 'yyyy-MM-dd', "en-US");

    let httpParams = new HttpParams().set('selectedBook', String(input.selectedBook.title))
      .set('startDate',startDate)
      .set('endDate', endDate)
      .set('culture', String(input.culture))
      .set('nature', String(input.nature))
      .set('recreation', String(input.recreation))
      .set('speed', String(input.speed))
      .set('budget', String(input.budget));
    return this.httpClient.get<ItineraryOutput>(`http://127.0.0.1:8081/itinerary`, { params: httpParams, responseType: 'json' });
  }
}

