import sys

actual_order_list = [1,2,3,4,5]
last = 0
next_p = 1
buffer = []

def check_and_send(incoming):
	# print(incoming)
	# print(buffer)
	if incoming in buffer:
		print("Sending : ",incoming)
		return True
	else:
		return False

for i in range(5):
	# Receive input
	line = input()
	flowletid = int(line)

	if flowletid == next_p:
		print("Sending : ",flowletid)
		next_p = next_p + 1
		while True:
			result = check_and_send(next_p)
			if result:
				next_p = next_p + 1
			else:
				break			
	else:
		buffer.append(flowletid)
		# print("Added to buffer")

print("all done")