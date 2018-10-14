import { Component, Inject } from '@angular/core';
import { QLogicService } from './qlogic.service'
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
//10.10.2.104

export interface DialogData {
  info: string;
  url: string;
}


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})


export class AppComponent {
  title: string;
  geoLoc: string;
  tags: Array<string>;
  responseText: string;

  selectedTab = 0;
  constructor(
    private qlogicService:QLogicService,
    public dialog: MatDialog) {
    this.title = '';
  }

  openFinalUrlDialog(url) {
    let dialogRef = this.dialog.open(DialogOverviewExampleDialog, {
      height: '400px',
      width: '600px',
      data: {info: "Your contract is successfully created, please remember the url before closing the window.", url : url}
    });
  }

  setPage(page) {
    this.selectedTab = page;
  }
}



@Component({
  selector: 'dialog-overview-example-dialog',
  templateUrl: 'dialog-overview-example-dialog.html',
})
export class DialogOverviewExampleDialog {

  constructor(
    public dialogRef: MatDialogRef<DialogOverviewExampleDialog>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData) {}

  onNoClick(): void {
    this.dialogRef.close();
  }

}