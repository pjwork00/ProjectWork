import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {BasicElement} from './serviceModels/BasicElement'

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient: HttpClient) { }


  public getInfo(): Observable<BasicElement>{
    return this.httpClient.get<BasicElement>(`http://127.0.0.1:8080`, {responseType: 'json'});
  }
}
