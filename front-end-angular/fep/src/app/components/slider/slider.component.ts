import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-slider',
  templateUrl: './slider.component.html',
  styleUrls: ['./slider.component.css']
})
export class SliderComponent implements OnInit {

  @Input() sliderText? : String;
  @Input() min? : String;
  @Input() max? : String;
  @Input() step? : String;
  @Input() value: number = 1;

  @Output() slideChange: EventEmitter<number> = new EventEmitter();

  constructor() { }

  ngOnInit(): void {
  }

  onSlideChange(event : any): void {
    this.value = event.value;
    this.slideChange.emit(this.value);
  }

}
