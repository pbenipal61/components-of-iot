import psutil
import datetime
import json
import time

run_loop_for_minutes = 1


def record_memory_usage():
    recording = {
        "time": time.time(),
        "cpu": psutil.cpu_percent(),
        "virtual-memory": psutil.virtual_memory(),
    }
    recordings_file = open("recordings.txt", "a")
    recordings_file.write(json.dumps(recording))
    recordings_file.close()


t_end = time.time() + 60 * run_loop_for_minutes
while time.time() < t_end:
    record_memory_usage()
    time.sleep(1)
