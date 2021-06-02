import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-slider',
  templateUrl: './slider.component.html',
  styleUrls: ['./slider.component.css']
})
export class SliderComponent implements OnInit {

  @Input() sliderText?: String;
  @Input() min?: String;
  @Input() max?: String;
  @Input() step?: String;
  @Input() value: number = 0;
  @Input() labelArray?: string[];

  @Output() slideChange: EventEmitter<number> = new EventEmitter();

  constructor() { }

  ngOnInit(): void {
  }

  onSlideChange(event: any): void {
    this.value = event.value;
    this.slideChange.emit(this.value);
  }


  formatThumbLabel(index: number): string {

    // [labelArray]="['Casual','Curious','Engaging','Rewarding']"
    var output: string = "" + index;
    if (this.labelArray != null && index <= this.labelArray.length) {
      output = this.labelArray[index];
    }
    return output;
  }



}
