import sys

#function to find the closest element to head
def nearest_to_head(head, requests):
    minimum = sys.maxint
    global close
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
    infile = open("test8.txt", "r")
    head, requests = infile.readlines()
    head = int(head)
    requests = requests.split(',')
    requests = [int(x) for x in requests]
    requests=sorted(requests)
    cost=[]
    service=[]
    first=0
    last=199
    number_of_req = len(requests)
    diff1 = abs(max(requests) - last)
    diff2 = abs(min(requests) - first)
    wait_time = 0
    close = nearest_to_head(head,requests)
    service.append(close)
    c = requests.index(close)
    requests.remove(close)
    if close <= head:
            requests_left = requests[:c]
            for i in reversed(requests_left):
                if i in requests:
                    service.append(i)
                    wait_time += abs(head - i)
                    head = i
                    requests.remove(i)
            if len(service) == number_of_req:
                print(','.join([str(x) for x in service]))
                print wait_time
                print str(service[len(service) - 1]) + "," + str(wait_time)
            else:
                wait_time += diff2
                index = first
                while (index <= last):
                    if index in requests:
                        service.append(index)
                        wait_time += abs(first - index)
                        first = index
                        requests.remove(index)
                    index = index + 1
                print(','.join([str(x) for x in service]))
                print wait_time
                print str(service[len(service) - 1]) + "," + str(wait_time)
    else:
        requests_right = requests[c:]
        for each in requests_right:
            if each in requests:
                service.append(each)
                wait_time += abs(head - each)
                head = each
                requests.remove(each)
        if len(service) == number_of_req:
            print(','.join([str(x) for x in service]))
            print wait_time
            print str(service[len(service) - 1]) + "," + str(wait_time)
        else:
            wait_time+= diff1
            index = last
            while(index>=0):
                if index in requests:
                    service.append(index)
                    wait_time+=abs(last-index)
                    last = index
                    requests.remove(index)
                index = index-1
            print(','.join([str(x) for x in service]))
            print wait_time
            print str(service[len(service)-1])+","+str(wait_time)