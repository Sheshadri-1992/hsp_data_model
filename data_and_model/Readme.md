Usage: python algorithm.py <num_packets> <payload_size> <qos_metric>

Eg: python algorithm.py 300 300 500

The above command will generate the recommendation of VNFs for flowlet of 300, with packet size being 300, with the QoS metric being 500

Output:

Counts fw 1, ids 2, aes 2
Latency : Overall latency : 436.42683956228126, fw 63.180445935326375, ids 119.38549084070002, aes 253.86090278625488

The counts indicate to meet the 500 ms latency, 1 instance each of fw, 2 each of ids and aes needs to be run. 
The Hybrid controller will orchestrate these number of instances through either IaaS/FaaS controller when executing the SFC for the flowlet of 300, with 300 payload size.

The predicted execution latency is 436 ms.
