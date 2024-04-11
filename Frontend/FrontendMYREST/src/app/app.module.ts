import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomepageComponent } from './homepage/homepage.component';
import { ReservationsComponent } from './reservations/reservations.component';
import { PrincipalComponent } from './principal/principal.component';
import { FeedbackComponent } from './feedback/feedback.component';
import {HashLocationStrategy, LocationStrategy} from "@angular/common";
import {FormsModule} from "@angular/forms";



@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
    ReservationsComponent,
    PrincipalComponent,
    FeedbackComponent
  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        FormsModule
    ],
  providers: [{ provide: LocationStrategy, useClass: HashLocationStrategy }],
  bootstrap: [AppComponent]
})
export class AppModule { }
