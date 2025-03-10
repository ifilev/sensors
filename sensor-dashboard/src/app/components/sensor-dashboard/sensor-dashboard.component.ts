import { Component, OnInit, OnDestroy } from '@angular/core';
import { SensorService } from '../../services/sensor.service';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { Subscription } from 'rxjs';

@Component({
  imports: [CommonModule],
  selector: 'app-sensor-dashboard',
  templateUrl: './sensor-dashboard.component.html',
  styleUrls: ['./sensor-dashboard.component.css']
})

export class SensorDashboardComponent implements OnInit, OnDestroy {
  sensorData: any[] = [];
  grafanaUrl: SafeResourceUrl = '';
  private socketSubscription: Subscription = new Subscription();

  constructor(private sanitizer: DomSanitizer, private sensorService: SensorService) {}

  ngOnInit(): void {
    // Grafana url
    const url = "http://localhost:3000/d/e683ceaf-93fa-48c8-a165-5f6249d3bc78/sensors?orgId=1&from=now-15m&to=now&refresh=auto&viewPanel=1"
    // link for the iframe
    this.grafanaUrl = this.sanitizer.bypassSecurityTrustResourceUrl(url);

    // subscribe for the web socket and receive data
    this.socketSubscription = this.sensorService.connectToRealTime().subscribe((data) => {
      this.sensorData = [...this.sensorData, ...data];
      // show only 10 records by default in the table
      if (this.sensorData.length > data.length) {
        // replace the old records with the new ones
        this.sensorData = this.sensorData.slice(data.length);
      }
    },
      (error) => {
        console.error("WebSocket error:", error);
    },
      () => {
        console.warn("WebSocket closed");
    });

//     this.fetchSensorData()
  }

  ngOnDestroy(): void {
    if (this.socketSubscription) {
      this.socketSubscription.unsubscribe();
      this.sensorService.closeConnection()
    }
  }

  fetchSensorData(): void {
    this.sensorService.getSensorData().subscribe((data) => {
      this.sensorData = data;
    });
  }
}
