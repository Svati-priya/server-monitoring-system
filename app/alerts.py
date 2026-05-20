import logging

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_cpu_alert(cpu_usage):
    if cpu_usage > 80:
        logging.warning(f"🚨 HIGH CPU ALERT: {cpu_usage}%")
    elif cpu_usage > 60:
        logging.info(f"⚠ CPU WARNING: {cpu_usage}%")

def check_memory_alert(memory_usage):
    if memory_usage > 80:
        logging.warning(f"🚨 HIGH MEMORY ALERT: {memory_usage}%")
    elif memory_usage > 60:
        logging.info(f"⚠ MEMORY WARNING: {memory_usage}%")

def check_disk_alert(disk_usage):
    if disk_usage > 85:
        logging.warning(f"🚨 LOW DISK SPACE ALERT: {disk_usage}%")