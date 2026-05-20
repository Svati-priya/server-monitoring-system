# 🚀 Server Monitoring & Alerting System

A lightweight **SRE-style backend monitoring system** built using Python and FastAPI.  
This project tracks system performance metrics like CPU, memory, and disk usage and provides real-time alerts using logging.

---

## 📌 About the Project

This project is designed to simulate a real-world **observability and monitoring system** used in production environments.

It helps in understanding how backend systems are monitored in DevOps/SRE roles using metrics, alerts, and system health checks.

The system collects real-time data from the machine using Python libraries and exposes it through REST APIs.

---

## 🧠 Key Learnings

- Backend API development using FastAPI
- System monitoring using psutil
- Logging and alert system design
- Understanding observability in SRE
- Basic DevOps and infrastructure concepts
- Docker-based deployment readiness

---

## 🛠 Tech Stack

- Python 🐍
- FastAPI ⚡
- psutil 📊
- Docker 🐳

---

## 📡 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home route |
| `/health` | Health check |
| `/metrics` | CPU, Memory, Disk usage |
| `/uptime` | System uptime |

---

## 🚨 Alert System

The system generates alerts when:

- CPU usage > 80%
- Memory usage > 80%
- Disk usage > 85%

All alerts are stored in `server.log`.

---

## 📊 Example Response

```json
{
  "cpu_usage": "12%",
  "memory_usage": "45%",
  "disk_usage": "60%"
}