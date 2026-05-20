from fastapi import FastAPI
from app.monitoring import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_system_uptime
)

from app.alerts import (
    check_cpu_alert,
    check_memory_alert
)

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Server Monitoring System Running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/metrics")
def metrics():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    check_cpu_alert(cpu)
    check_memory_alert(memory)
    check_disk_alert(disk)

    return {
        "cpu_usage": f"{cpu}%",
        "memory_usage": f"{memory}%",
        "disk_usage": f"{disk}%"
    }

@app.get("/uptime")
def uptime():
    return {
        "uptime": get_system_uptime()
    }