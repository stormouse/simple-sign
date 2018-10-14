import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule } from '@angular/forms';
import { MatButtonModule, MatTabsModule, MatCardModule, MatMenuModule, MatToolbarModule, MatIconModule, MatListModule, MatFormFieldModule, MatGridListModule, MatInputModule } from '@angular/material';
import { AutosizeModule } from 'ngx-autosize';
import { MatDialogModule } from '@angular/material/dialog';
import { Ng4LoadingSpinnerModule } from 'ng4-loading-spinner';

import { AppComponent, DialogOverviewExampleDialog } from './app.component';
import { TitleEditComponent } from './title-edit/title-edit.component';
import { MatdashComponent } from './matdash/matdash.component';
import { LayoutModule } from '@angular/cdk/layout';
import { UploadComponent } from './upload/upload.component';


@NgModule({
  declarations: [
    AppComponent,
    TitleEditComponent,
    MatdashComponent,
    UploadComponent,
    DialogOverviewExampleDialog,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    HttpModule,
    FormsModule,
    MatFormFieldModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatCardModule, 
    MatMenuModule, 
    MatToolbarModule, 
    MatListModule,
    MatIconModule, 
    MatGridListModule, 
    LayoutModule,
    MatInputModule,
    MatTabsModule,
    AutosizeModule,
    MatDialogModule,
    Ng4LoadingSpinnerModule,
    Ng4LoadingSpinnerModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
