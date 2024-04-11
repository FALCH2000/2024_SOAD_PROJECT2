import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
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

  reserve(reservacion: any): Observable<any> {
    const url = 'https://us-central1-groovy-rope-416616.cloudfunctions.net/gestionar_reservacion/reservar';

    // Configuración de encabezados para resolver el problema de CORS
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
        'withCredentials': 'true'
      })
    };

    return this.http.post<any>(url, reservacion, httpOptions);
  }
}
