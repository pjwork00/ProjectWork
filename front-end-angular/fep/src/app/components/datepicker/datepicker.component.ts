import { Component, Input, OnInit,EventEmitter, Output, OnChanges } from '@angular/core';
import { MatDatepickerInputEvent } from '@angular/material/datepicker';


@Component({
  selector: 'app-datepicker',
  templateUrl: './datepicker.component.html',
  styleUrls: ['./datepicker.component.css']
})
export class DatepickerComponent implements OnInit {

  @Input() placeholderText? : String;
  @Input() inputDate? : Date;
  @Output() dateChange: EventEmitter<Date> = new EventEmitter();

  //inputDate? : Date;


  constructor() {
    //this.inputDate = this.inputDateIn;
   }

  ngOnInit(): void {
  }

  onDateChange(): void {
    this.dateChange.emit(this.inputDate);
  }

}
