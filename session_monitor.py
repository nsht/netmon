import datetime
import signal
import sys
import time

import psutil


ERASE_LINE = "\033[2K"


class Monitor:
    def __init__(self):
        self.initial_data = 0

    def monitor(self):
        start_time = datetime.datetime.now().strftime("%H:%M:%S %d %B %Y")
        print(f"Monitoring Started on {start_time}")
        self.initial_data = self.get_data_used()
        while True:
            time.sleep(1)
            data = self.get_data_used()
            print(ERASE_LINE, end="\r", flush=True)
            print(f"Data Usage {data} mb", end="\r")

    def signal_handler(self, sig, frame):
        data = self.get_data_used()
        diff = data - self.initial_data
        print(ERASE_LINE, end="\r", flush=True)
        print(f"Total data used this session is {diff} mb")
        sys.exit(0)

    def get_data_used(self):
        data_obj = psutil.net_io_counters(pernic=True)
        return data_obj["enp3s0"].bytes_recv / 1000 // 1000


if __name__ == "__main__":
    mon = Monitor()
    signal.signal(signal.SIGINT, mon.signal_handler)
    mon.monitor()

