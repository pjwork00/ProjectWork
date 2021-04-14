import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HomePageInputForm } from './models/homePageInputForm';
import { BasicElement } from './serviceModels/BasicElement';
import {formatDate} from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) { }


  public getInfo(): Observable<BasicElement> {
    return this.httpClient.get<BasicElement>(`http://127.0.0.1:8080/`, { responseType: 'json' });
  }



  public getItinerary(input: HomePageInputForm): Observable<BasicElement> {

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
    return this.httpClient.get<BasicElement>(`http://127.0.0.1:8080/itinerary`, { params: httpParams, responseType: 'json' });
  }
}

