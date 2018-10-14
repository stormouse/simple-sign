import { Component, OnInit, EventEmitter, Input, Output } from '@angular/core';
import { QLogicService } from '../qlogic.service';
import { Ng4LoadingSpinnerService } from 'ng4-loading-spinner';

@Component({
  selector: 'app-matdash',
  templateUrl: './matdash.component.html',
  styleUrls: ['./matdash.component.css']
})
export class MatdashComponent {
  titles: Array<string>;
  contents: Array<string>;
  @Output() showUrlEvent = new EventEmitter<string>();
  urlStr: string;

  ngOnInit() {
    this.titles = new Array<string>();
    this.contents = new Array<string>();
    this.qlogicService.googleFormSubject.subscribe(()=>{this.loadActualData()});
  }

  loadActualData(): void {
    let data = JSON.parse(this.qlogicService.googleForm);
    let items = data.itemList;
    for(let i = 0; i < items.length; i++) {
      this.titles.push(items[i].title);
      this.contents.push(items[i].content);
      if(items[i].itemType == "multipleChoice") {
        for(let j = 0; j < items[i].choices[0].subItems.length; j++) {
          this.titles.push(items[i].choices[0].subItems[j].title);
          this.contents.push(items[i].choices[0].subItems[j].content);
        }
      }
    }
  }

  trackByFn(index: number, value: any) {
    return index;
  }

  submitReview() {
    this.qlogicService.sendGoogleForm((res)=>{
      //this.showUrlEvent.next(res['publishedUrl']);
      this.urlStr = res['publishedUrl'];
      this.spinnerService.hide();
    });
    this.spinnerService.show();
  }

  constructor(
    private qlogicService:QLogicService, 
    private spinnerService: Ng4LoadingSpinnerService) {}
}
