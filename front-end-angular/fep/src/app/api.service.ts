import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HomePageInputForm } from './models/homePageInputForm';
import { BasicElement } from './serviceModels/BasicElement'

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) { }


  public getInfo(): Observable<BasicElement> {
    return this.httpClient.get<BasicElement>(`http://127.0.0.1:8080/`, { responseType: 'json' });
  }



  public getItinerary(input: HomePageInputForm): Observable<BasicElement> {

    let httpParams = new HttpParams().set('selectedBook', String(input.selectedBook))
      .set('numberOfDays', String(input.numberOfDays))
      .set('numberOfPeople', String(input.numberOfPeople));
    return this.httpClient.get<BasicElement>(`http://127.0.0.1:8080/itinerary`, {params: httpParams, responseType: 'json' });
  }
}

