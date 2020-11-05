import random
import threading
import time
import queue

import account

pipeline = queue.Queue()

def account_feeder():
	while True:
		if (credentials := account.create_account()):
			pipeline.put(credentials)
			print(pipeline.qsize())
		time.sleep(random.randint(3, 10))

def start_feeder_worker(feeders=20):
	for _ in range(feeders):
		worker = threading.Thread(target=account_feeder)
		worker.setDaemon(True)
		worker.start()
