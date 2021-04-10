import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ItineraryPageComponent } from './pages/itinerary-page/itinerary-page.component';
import { HomePageComponent } from './pages/home-page/home-page.component';

const routes: Routes = [
  {
    path: 'itineraryPage',
    component: ItineraryPageComponent
  },
  {
    path: 'homePage',
    component: HomePageComponent
  },
  {
    path: '',   redirectTo: '/homePage', pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
