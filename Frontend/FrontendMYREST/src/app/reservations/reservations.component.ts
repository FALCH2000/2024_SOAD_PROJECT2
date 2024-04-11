import { Component } from '@angular/core';
import { ReservationsService } from '../services/reservations.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-reservations',
  templateUrl: './reservations.component.html',
  styleUrls: ['./reservations.component.scss']
})
export class ReservationsComponent {
  menuData!: {  };
  selectedItems: string[] = [];
  menuCategories!: string[];
  disponibilidad = new Array<any>();

  constructor(private reservationService:ReservationsService, private http: HttpClient){}
  
  ngOnInit(): void {
    
    this.reservationService.getDisponibilidad().subscribe((data)=>{
      this.disponibilidad = data.data;
      console.log(this.disponibilidad);
    }) 

    /*this.http.get<any>('/assets/disponibilidad.json').subscribe(data => {
      this.menuData = data;
      this.menuCategories = Object.keys(this.menuData);
      console.log(this.menuData)
    }); */

    
  }
}
