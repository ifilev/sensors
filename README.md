#Sensor Monitoring System

##Overview
This project is a sensor monitoring system built using **FastAPI (Python)** for the backend, **Angular** for the frontend, and **PostgreSQL** as the database.
**Grafana** is used for real-time data visualization.

##Setup & installation
### 1️. Clone the repository
```bash
git clone <repo_url>
```
You will need to have a docker installed.

### 2. Build and run the Docker containers
```bash
docker-compose up --build -d
```
This will start:
- FastAPI backend container
- Angular frontend container
- PostgreSQL database
- Grafana 


## Accessing the Services
| Service | URL |
|---------|-----|
| **FastAPI** (Docs) | [http://localhost:8000/docs](http://localhost:8000/docs) |
| **Angular Frontend** | [http://localhost:4200/browser/](http://localhost:4200/browser/) |
| **Grafana Dashboard** | [http://localhost:3000](http://localhost:3000) user: **admin** pass: **qwerty**|
| **PostgreSQL** | `docker exec -it db psql -U ivan -d sensordb` |
<br />
If you can't access the backend, restart the container.

```bash
docker-compose restart <service_name>
```

#### **Stop and Remove Containers**
```bash
docker-compose down
```

##  How the system is working
When you open the http://localhost:4200/browser/ a WebSocket connection is opened
which starts the sensor data generation every 10 seconds. The data is presented
in the table (up to 10 records). The table is updated when new data is received.