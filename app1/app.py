import time
import re
from datetime import datetime

LOG_PATH = "/var/log/syslog"
OUTPUT_FILE = "/shared/errors.log"

print("Log reader started. Checking every 60 seconds...")

while True:
    try:
        with open(LOG_PATH, "r") as log_file:
            logs = log_file.readlines()

        errors = [line for line in logs if re.search(r'info|warning|error|fail|critical', line, re.IGNORECASE)]

        with open(OUTPUT_FILE, "w") as f:
            if errors:
                for e in errors:
                    f.write(e)
            else:
                f.write(f"{datetime.now()} - No errors found\n")

        print(f"Updated {OUTPUT_FILE} with {len(errors)} errors.")

    except Exception as e:
        print(f"Error reading logs: {e}")

    time.sleep(60)