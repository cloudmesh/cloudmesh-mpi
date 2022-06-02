from random import randint
from cloudmesh.common.console import Console
import argparse
import time

parser = argparse.ArgumentParser(description='A test program for mpi.')

parser.add_argument("--sleep_length", help="Two numbers separated by commas. The first is the "
                                         "shortest length to sleep. The second is the longest "
                                         "to sleep.",
                    default="1,3")

args = parser.parse_args()

#print(args.sleep_length)

if not "," in args.sleep_length:
    Console.error("comma not found in argument. Defaulting to 1,3 seconds.")
    args.sleep_length = "1,3"

list = args.sleep_length.split(",")

#print(list)

value = randint(int(list[0]), int(list[1]))
#print(value)
time.sleep(value)