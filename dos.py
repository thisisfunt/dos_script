import requests
from threading import Thread
from sys import argv

thread_count = argv[2]

def TreadFunc():
	i = 0
	while True:
		requests.get(argv[1])
		i += 1
		print("request", i)

threads = [Thread(target=TreadFunc) for i in range(4)]


for i in range(len(threads)):
	threads[i].start()