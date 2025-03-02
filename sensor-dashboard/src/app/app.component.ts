import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SensorDashboardComponent } from './components/sensor-dashboard/sensor-dashboard.component';


@Component({
  selector: 'app-root',
  imports: [RouterOutlet, SensorDashboardComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'sensor-dashboard';
}
