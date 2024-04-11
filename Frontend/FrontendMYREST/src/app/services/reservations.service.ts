import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReservationsService {

  constructor(private http:HttpClient) { }

  getDisponibilidad():Observable<any>{
    const url = 'https://1wqnzfrr-8080.use2.devtunnels.ms/disponibilidad';
    return this.http.get<any>(url);
  }
}
