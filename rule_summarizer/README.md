NOTE: This folder contains scripts for generating QoS rule summary, based on the VNF recommendations from the Auto-rec module

1. Usage :python rule_summarizer.py 500_qos_rules.csv 
	 500ms is the time-budget for which auto-rec module presented VNF recommendations
	 

2. Entries inside 500_qos_rules.csv file
	First row entries are payload size
	First column entries are flowlet size
	Rest are all VNF instance recommendations from auto-rec in the order fw, ids, ec 
	E.g. if 223 is the entry, 2 fw, 2 ids, 3 aes instances are the recommendations to meet 500ms qos metric, for a given flowlet, payload range

3. Resource files
	r1, r2, r3 are the resource files to which VNF recommendations are matched against
	This is a static mapping, but it is flexible enough to be changed in accordance to available instance types/size in public Cloud providers

