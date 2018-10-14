import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Section } from './section'
import { Subject } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};


@Injectable({
  providedIn: 'root'
})

export class QLogicService {
  
  sections: Array<Section> = new Array<Section>();
  tags: Array<string> = new Array<string>();
  govern: Map<string, Array<number>> = new Map<string, Array<number>>(); 
  googleForm: string;
  googleFormSubject = new Subject();

  constructor(private http:HttpClient) { }

  getGeoLocation(callback) {
    this.http.get("http://ip-api.com/json", httpOptions).subscribe((res:Response) => callback(res));
  }

  parseContractText(data, callback) {
    this.http.post("http://localhost:8080/parse_contract", {data: data}, httpOptions).subscribe(
      (res:Response) => {
        this.initQuestionLogic(res); 
        this.googleForm = this.buildGoogleForm(); 
        this.googleFormSubject.next(this.googleForm);
        callback(res)}
    );
  }

  initQuestionLogic(data): void {
    this.govern.clear();
    for(let i = 0; i < data.sections.length; i++){
      this.sections[i] = new Section(i, data.sections[i].content, data.sections[i].triggers);
      for(let tag of data.sections[i].triggers) {
        if(this.tags.indexOf(tag) == -1)
          this.tags.push(tag);
        if(!(tag in this.govern)) this.govern[tag] = [];
        this.govern[tag].push(i);
      }
    }
  }

  getTags(): Array<string> {
    return this.tags;
  }


  buildGoogleForm(): string {
    let numSections = this.sections.length;
    let sectionIncluded = new Array<boolean>(numSections).fill(false);
    let listItems = [];
    for(let i=0;i<numSections;i++) {
      if(sectionIncluded[i]) continue;
      for(let tag of this.sections[i].triggers) {
        if(tag == 'EVERY_TIME') {
          listItems.push({
            itemType: 'info',
            title: 'You need to know',
            content: this.sections[i].content,
          });
          sectionIncluded[i] = true;
        } else {
          let subItems = [];
          for(let j of this.govern[tag]) {
            subItems.push({
              itemType: "info",
              title: "About " + tag,
              content: this.sections[j].content,
            });
            sectionIncluded[j] = true;
          }
          let question = {
            itemType: "multipleChoice",
            title: 'Concerned about ' + tag + "?",
            hasSubItem: true,
            choices : [
              {
                choiceVal: "Yes",
                subItems: subItems,
              },
              {
                choiceVal: "No",
              }]
          };
          listItems.push(question);
        }
      }
    }

    let data = {
      title: 'Contract',
      itemList: listItems
    };

    return JSON.stringify(data);
  }


  sendGoogleForm(callback) {
    let url = "http://localhost:8080/send_google_form"; //"https://script.google.com/macros/s/AKfycbzNT3dOWdGU4Fy_UVx9QeD_Ute3HJNETf8ZHEgwdymMGUOLkB0m/exec";
    this.http.post(url, this.googleForm, httpOptions).subscribe((res:Response)=>{callback(res)});
  }
}

