"""
Demonstrates how to use the gevent compatible scheduler to schedule a job that executes on 3 second
intervals.
"""

import os
from datetime import datetime

from apscheduler.schedulers.gevent import GeventScheduler


def tick():
    print(f"Tick! The time is: {datetime.now()}")


if __name__ == "__main__":
    scheduler = GeventScheduler()
    scheduler.add_job(tick, "interval", seconds=3)
    g = scheduler.start()  # g is the greenlet that runs the scheduler loop
    print("Press Ctrl+{} to exit".format("Break" if os.name == "nt" else "C"))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        g.join()
    except (KeyboardInterrupt, SystemExit):
        pass
