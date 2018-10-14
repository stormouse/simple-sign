import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-title-edit',
  templateUrl: './title-edit.component.html',
  styleUrls: ['./title-edit.component.css']
})

export class TitleEditComponent implements OnInit {

  titles: Array<string>;

  constructor() { }

  ngOnInit() {
    this.titles = new Array<string>(10).fill("dummy");
  }

  trackByFn(index: number, value: any) {
    return index;
  }

}
