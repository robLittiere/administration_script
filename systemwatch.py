import os
from datetime import datetime
import psutil
import threading
import logging

logging.getLogger().setLevel(logging.INFO)


def print_system_info(interval):
    thread = threading.Timer(interval, print_system_info, [interval])
    thread.start()
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    logging.info("Date : " + dt_string)
    logging.info("CPU Numbers : " + str(psutil.cpu_count()))
    logging.info("Usage : " + str(psutil.cpu_percent(interval=1)) + "%")
    logging.info(psutil.cpu_times())
    logging.info(psutil.cpu_stats())
    logging.info(psutil.cpu_freq())

    logging.info("Memory Metrics : ")
    logging.info(psutil.virtual_memory())
    logging.info("Swap metrics : ")
    logging.info(psutil.swap_memory())

    logging.info("Disk metrics :")
    logging.info(psutil.disk_partitions())
    logging.info(psutil.disk_usage(path='/'))

    # print("Network Metrics : ")
    # print(psutil.net_io_counters())
    # print(psutil.net_if_addrs())
    # print(psutil.net_if_stats())

    logging.info("Users : ")
    logging.info(psutil.users())


def log_system_info_to_file(interval, filepath):
    thread = threading.Timer(interval, log_system_info_to_file, [interval, filepath])
    thread.start()

    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    logging.basicConfig(filename=filepath, encoding='utf-8', level=logging.DEBUG)
    logging.info("Date : " + dt_string)
    logging.info("CPU Numbers : " + str(psutil.cpu_count()))
    logging.info("CPU Numbers : " + str(psutil.cpu_count()))
    logging.info("Usage : " + str(psutil.cpu_percent(interval=1)) + "%")
    logging.info(psutil.cpu_times())
    logging.info(psutil.cpu_stats())
    logging.info(psutil.virtual_memory())
    logging.info(psutil.swap_memory())
    logging.info(psutil.disk_partitions())
    logging.info(psutil.disk_usage('/'))
    logging.info('\n')
