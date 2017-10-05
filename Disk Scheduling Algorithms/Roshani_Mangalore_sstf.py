import sys

#function to find the closest element to head
def nearest_to_head(head, requests):
    minimum = sys.maxint
    for i in requests:
        if abs(head - i) < minimum:
            minimum = abs(head - i)
            close = i
        if abs(head - i) == minimum:
            close = min(i, close)
    return close

#main fuction
if __name__ == '__main__':
    requests = []
    infile = open(sys.argv[1], "r")
    head=int(infile.readline())
    cost=[]
    service=[]
    for line in infile:
         requests= sorted(map(int, line.split(',')))
    for i in range(0,len(requests)):
        close = nearest_to_head(head,requests)
        diff = abs(head - close)
        head = close
        service.append(close)
        cost.append(diff)
        requests.remove(close)
    print(','.join([str(x) for x in service]))
    print sum(cost)
    print str(service[len(service) - 1]) + "," + str(sum(cost))
