import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-info',
  templateUrl: './info.component.html',
  styleUrls: ['./info.component.css']
})
export class InfoComponent implements OnInit {

  info? : string; 

  constructor(private apiService: ApiService) { }


  ngOnInit(): void {
    this.apiService.getInfo().subscribe((data)=>{
      this.info = "" + data.basicElement;
    });
  }


  getInfo(){
    console.log(this.info);
  }
}
