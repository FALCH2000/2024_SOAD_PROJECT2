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
  available_tables:any = new Array<any>();
  selectedHour = ""
  selectedDay = ""
  selectedTable = ""

  name = '';
  id = '';

  constructor(private reservationService:ReservationsService, private http: HttpClient){}

  ngOnInit(): void {

    this.reservationService.getDisponibilidad().subscribe((data)=>{
      this.disponibilidad = data.data.disponibilidad;
      console.log(this.disponibilidad);
    })

    /*this.http.get<any>('/assets/disponibilidad.json').subscribe(data => {
      this.menuData = data;
      this.menuCategories = Object.keys(this.menuData);
      console.log(this.menuData)
    }); */
  }

  selectHour(hour: any, day: any){
    this.selectedHour = hour.hora;
    this.selectedDay = day.dia;
    this.available_tables = [];
    this.selectedTable = "";
    for(let i = 1; i < 11; i++){
      if(hour.mesas[i] == true){
        this.available_tables.push(i);
      }
    }
    console.log(this.available_tables);
  }
  selectTable(table: any){
    this.selectedTable = table;
    console.log(this.selectedTable);
  }

  reserve(){
    if(this.selectedTable != "" && this.selectedDay != "" && this.selectedHour != ""
    && this.name != "" && this.id != "") {
      const reserva = {
        "dia": this.selectedDay,
        "hora": this.selectedHour,
        "mesa": this.selectedTable,
        "nombre": this.name,
        "cedula": this.id
      }
      console.log(reserva);
      this.reservationService.reserve(reserva).subscribe((data)=>{
        if(data.status_code == 200){
          alert("Reservado");
          console.log(data);
        }
        else{
          alert("Error al reservar");
          console.log(data);
        }

      });

    }
    else{
      alert("Por favor llene todos los campos")
    }
  }

  goBack(){
    this.selectedHour = "";
    this.selectedDay = "";
    this.selectedTable = "";
    this.name = "";
    this.id = "";

  }

}
