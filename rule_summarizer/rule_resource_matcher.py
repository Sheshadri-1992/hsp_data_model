import sys
import json

def retrieve_resource_for_rules(rule: str):

	max_instance = 1
	for i in range(0,len(rule)):
		if int(rule[i]) > max_instance:
			max_instance = int(rule[i])

	'''
	Static mapping of max instance to resources
	'''

	resource_dict = ""
	with open("r"+str(max_instance)+".json", "r") as res_file:
		resource_dict = res_file.read()
		resource_dict = resource_dict.strip("\n")

	resource_spec = "|" + resource_dict + " | { fw : "+ rule[0] + ", ids : "+ rule[1] + ", aes : " + rule[2] +" }"
	return resource_spec

#	print(retrieve_resource_for_rules("111"))