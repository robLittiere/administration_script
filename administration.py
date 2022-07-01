import psutil
import argparse
import threading
import systemwatch
import logging
from RepeatedTimer import RepeatedTimer
import os

logging.getLogger().setLevel(logging.INFO)
my_parser = argparse.ArgumentParser(prog="Robin's Administration Script",
                                    description="Follow your computer's performance and metrics")
# Add the arguments
# Add groupe of exclusive arguments
my_parser.add_argument('--interval', '-i',
                             type=str, required=True,
                             help="Interval to log informations")


# Optionnal argument
my_parser.add_argument('--optional', '-o',
                       type=str, required=False,
                       help="The path of file to put the result")

# Optionnal argument
my_parser.add_argument('--filename', '-f',
                       type=str, required=False,
                       help="File path where to put the results")

# Execute the parse_args() method
args = my_parser.parse_args()

if args.interval and args.interval.isdigit():
    if args.filename:
        print("filename called")
        systemwatch.log_system_info_to_file(int(args.interval), args.filename)
    else :
        print("print called")
        systemwatch.print_system_info(int(args.interval))
else:
    logging.critical("No intervals given")
