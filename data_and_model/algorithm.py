import aes_model
import ids_model
import fw_model
import math
import sys
import time
import warnings
import psutil
warnings.filterwarnings("ignore", category=DeprecationWarning) 

MAX_LATENCY = 10000


def main():

	aes_count = 1
	ids_count = 1
	fw_count = 1
	turn = 0

	estimated_latency = MAX_LATENCY
	aes_estimated_latency = aes_obj.predict(num_packets, payload_size)
	ids_estimated_latency = ids_obj.predict(num_packets, payload_size)
	fw_estimated_latency = fw_obj.predict(num_packets, payload_size)

	estimated_latency = aes_estimated_latency + ids_estimated_latency + fw_estimated_latency

	while (aes_count < 5) and (estimated_latency > qos_metric):

		if turn == 0:
			aes_count = aes_count + 1
			new_num_packets = int(math.ceil(num_packets/aes_count))
			aes_estimated_latency = aes_obj.predict(new_num_packets, payload_size)
			estimated_latency = aes_estimated_latency + ids_estimated_latency + fw_estimated_latency
			turn = 1
			continue

		if turn == 1:
			ids_count = ids_count + 1
			new_num_packets = int(math.ceil(num_packets/ids_count))
			ids_estimated_latency = ids_obj.predict(new_num_packets, payload_size)
			estimated_latency = aes_estimated_latency + ids_estimated_latency + fw_estimated_latency
			turn = 2
			continue

		if turn == 2:
			fw_count = fw_count + 1
			new_num_packets = int(math.ceil(num_packets/fw_count))
			fw_estimated_latency = fw_obj.predict(new_num_packets, payload_size)
			estimated_latency = aes_estimated_latency + ids_estimated_latency + fw_estimated_latency
			turn = 0
			continue

	print("Counts fw {0}, ids {1}, aes {2}".format(fw_count, ids_count, aes_count))
	print("Latency : Overall latency : {0}, fw {1}, ids {2}, aes {3}".format(estimated_latency, fw_estimated_latency, ids_estimated_latency, aes_estimated_latency))

if __name__ == '__main__':

	if len(sys.argv) != 4:
		print("Usage: python algorithm.py <num_packets> <payload_size> <qos_metric>")
		exit(0)

	aes_obj = aes_model.AES()
	aes_obj.train_module()
	ids_obj = ids_model.IDS()
	ids_obj.train_module()
	fw_obj = fw_model.Firewall()
	fw_obj.train_module()

	print("Trained all models")

	num_packets = int(sys.argv[1])
	payload_size = int(sys.argv[2])
	qos_metric = int(sys.argv[3])

	start_time = time.time()
	for i in range(1):
		main()
		#time.sleep(1)
	
	result = psutil.cpu_percent()	
	end_time = time.time()
	total_time = (end_time - start_time)*1000 
	print("Total time : {0}".format(total_time))	
