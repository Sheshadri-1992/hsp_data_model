import sys
import rule_resource_matcher

if len(sys.argv) != 2:
	print("python rule_summarizer.py <qos_rule_file.csv>")
	exit(0)

my_file = open(sys.argv[1], "r")
lines = my_file.readlines()

row_length = len(lines)
col_length = len(lines[0].split(","))

print(row_length, col_length)

rule_2d = []

payload_size_list = [ int(x) for x in lines[0].split(",") ]
flowlet_size_list = []

for line in lines:

	vnf_rec_list = line.split(",")
	flowlet_size_list.append(int(vnf_rec_list[0]))
	line = [x.strip() for x in line.split(",")]
	rule_2d.append(line)


for i in range(0, col_length):
	rule_2d[0][i] = int(rule_2d[0][i])

for j in range(0, row_length):
	rule_2d[j][0] = int(rule_2d[j][0])

start_rule = "111"
rule_number = 1
rule_dict = {}
rule_dict[start_rule] = 1


for col_index in range(1, col_length):
	start_payload_size = rule_2d[0][col_index-1]
	start_flowlet_size = rule_2d[0][0]
	print("\n")
	
	for row_index in range(2, row_length):

		next_rule = rule_2d[row_index][col_index]		
		if next_rule == start_rule:
			continue
		else:			
			print("if {0} < flowlet < {1} and {2} payload_size < {3} then --> rule {4} {5}".format(start_flowlet_size, rule_2d[row_index][0], 
				start_payload_size, rule_2d[0][col_index], rule_dict[start_rule], rule_resource_matcher.retrieve_resource_for_rules(start_rule)))
			start_flowlet_size = rule_2d[row_index][0]
			start_rule = rule_2d[row_index][col_index]
			if next_rule not in rule_dict:				
				rule_number = rule_number + 1
				rule_dict[next_rule] = rule_number


	print("if {0} < flowlet < {1} and {2} payload_size < {3} then --> rule {4} {5}".format(start_flowlet_size, rule_2d[row_index][0], 
				start_payload_size, rule_2d[0][col_index], rule_dict[start_rule], rule_resource_matcher.retrieve_resource_for_rules(start_rule)))


