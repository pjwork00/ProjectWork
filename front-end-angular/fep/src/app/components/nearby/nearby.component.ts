import { Component, Input, OnInit } from '@angular/core';
import { HomePageInputForm } from 'src/app/models/homePageInputForm';

@Component({
  selector: 'app-nearby',
  templateUrl: './nearby.component.html',
  styleUrls: ['./nearby.component.css']
})
export class NearbyComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  @Input() homePageInputForm : HomePageInputForm = new HomePageInputForm;

}
