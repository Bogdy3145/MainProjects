import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { GetcontentComponent } from './components/getcontent/getcontent.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './components/login/login.component';
import { FormsModule } from '@angular/forms';

import { AddcontentComponent } from './components/addcontent/addcontent.component';


@NgModule({
  declarations: [
    AppComponent,
    GetcontentComponent,
    LoginComponent,
    AddcontentComponent
  ],
  imports: [
    FormsModule,
    HttpClientModule,
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
