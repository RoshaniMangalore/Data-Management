# INF551
Scheduling Algorithms in Python (SSTF, SCAN and F-SCAN)
implementation in Python for the following disk scheduling algorithms:
SSTF, SCAN, and F-SCAN (a new algorithm). F-SCAN is a variant of SCAN that addresses the potential
starvation problem in the SSTF and SCAN algorithms. Recall that in SSTF and SCAN, there is a single
queue containing all the requests, including those that are dynamically arriving. F-SCAN instead
maintains two queues Q1 and Q2. Before serving the requests, it freezes the queue Q1 which contains
all requests currently outstanding. It can moves the head to serve all requests in Q1 just like SCAN. All
new requests will be placed into Q2. When it finishes all requests in Q1, it will move all requests in Q2 to
Q1. It then starts the “freeze, serve, and move” cycle. F-SCAN is mentioned in the page 11 of reading
chapter. Wikipedia has a bit more details too: https://en.wikipedia.org/wiki/FSCAN.
