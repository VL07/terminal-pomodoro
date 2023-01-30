#!/usr/local/bin/python3

import sys
import time
import os
import math

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[0;31m"

SELECTED = "■"
NOT_SELECTED = "□"

def main():
	if len(sys.argv) != 3:
		print("Expected 2 arguments: <work time: minutes> <rest time: minutes>")
		return

	workTime = sys.argv[1]
	restTime = sys.argv[2]

	try:
		workTime = int(workTime) * 60
		restTime = int(restTime) * 60
	except ValueError:
		print("Unable to convert either work time of rest time to a number")

	working = True
	started = time.time()

	while True:
		os.system("clear")

		if working:
			remaining = started + workTime - time.time()

			print(f"{BOLD}WORKING{RESET}")
			print(f"{math.floor(remaining / 60)}:{round(remaining % 60)} {(NOT_SELECTED * math.floor((remaining / workTime) * 10)):{SELECTED}<10}")

			if remaining < 0:
				started = time.time()
				working = False

		else:
			remaining = started + restTime - time.time()

			print(f"{BOLD}RESTING{RESET}")
			print(f"{math.floor(remaining / 60)}:{round(remaining % 60)} {(NOT_SELECTED * math.floor((remaining / restTime) * 10)):{SELECTED}<10}")

			if remaining < 0:
				started = time.time()
				working = True

		
		time.sleep(1)

if __name__ == "__main__":
	main()