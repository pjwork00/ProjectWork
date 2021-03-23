import { Component, OnInit } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent implements OnInit {

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
