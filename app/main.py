from fastapi import FastAPI
from app.monitoring import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_system_uptime
)

from app.alerts import (
    check_cpu_alert,
    check_memory_alert,
    check_disk_alert
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server Monitoring System Running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    try:
        cpu = get_cpu_usage()
        memory = get_memory_usage()
        disk = get_disk_usage()

        return {
            "cpu_usage": cpu,
            "memory_usage": memory,
            "disk_usage": disk
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/uptime")
def uptime():
    return {
        "uptime": get_system_uptime()
    }