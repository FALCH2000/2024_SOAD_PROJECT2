import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomepageComponent } from './homepage/homepage.component';
import { PrincipalComponent } from './principal/principal.component';
import { ReservationsComponent } from './reservations/reservations.component';
import { FeedbackComponent } from './feedback/feedback.component';

const routes: Routes = [
  {path: '', redirectTo:'/principal', pathMatch: 'full'},
  { path: 'homepage', component: HomepageComponent },
  { path: 'principal', component: PrincipalComponent },
  { path: 'reservacion', component: ReservationsComponent },
  { path: 'feedback', component: FeedbackComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
