import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { WebSocketSubject } from 'rxjs/webSocket';

@Injectable({
  providedIn: 'root',
})

export class SensorService {
  private apiUrl = 'http://localhost:8000';
  private socket$!: WebSocketSubject<any>;

  constructor(private http: HttpClient) {}

  getSensorData(): Observable<any> {
    return this.http.get<any>(this.apiUrl + '/sensor_data');
  }

//   connectToRealTime(): WebSocketSubject<any> {
//     if (!this.socket$ || this.socket$.closed) {
//       this.socket$ = new WebSocketSubject({
//         url: `${this.apiUrl.replace('http', 'ws')}/realtime`,
//         deserializer: (e) => JSON.parse(e.data), // Fix JSON deserialization
//       });
//     }
//     return this.socket$;
//   }

  connectToRealTime(): WebSocketSubject<any> {
    if (!this.socket$) {
      this.socket$ = new WebSocketSubject(`${this.apiUrl.replace('http', 'ws')}/realtime`);
    }
    console.log(this.socket$)
    return this.socket$;
  }

  getMessages(): Observable<any> {
    return this.socket$.asObservable();
  }

  closeConnection() {
    if (this.socket$) {
      this.socket$.complete();
    }
  }
}
