import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReservationsService {

  constructor(private http:HttpClient) { }

  getDisponibilidad():Observable<any>{
    const url = 'https://us-west1-groovy-rope-416616.cloudfunctions.net/reservacion/disponibilidad';
    
    return this.http.get<any>(url);
  }
}
