import { Component, OnInit, EventEmitter, Input, Output } from '@angular/core';
import { QLogicService } from '../qlogic.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {

  textfile: string;
  @Output() changeTabEvent = new EventEmitter<number>();

  constructor(private qlogicService:QLogicService) { }

  ngOnInit() {
  }

  submitDocument(): void {
    this.qlogicService.parseContractText({"file": this.textfile}, ()=>{this.changeTabEvent.next(1);});
  }

}
