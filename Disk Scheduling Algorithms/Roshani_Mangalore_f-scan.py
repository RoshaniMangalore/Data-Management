import sys
global schedule

#function to find the closest element to head
def closest_to_head(head, initial_reqs):
    minimum = sys.maxint
    return_val = sys.maxint
    for x in initial_reqs:
        if abs(head - x) < minimum:
            minimum = abs(head - x)
            return_val = x
        if abs(head - x) == minimum:
            return_val = min(x, return_val)
    return return_val

#function to implement scan scheduling algorithm
def scan(head, initial_req, first, last):
    global schedule
    number_of_req = len(initial_req)
    diff1 = abs(max(initial_req) - last)
    diff2 = abs(min(initial_req) - first)
    wait_time = 0
    service_req = []
    initial_req = sorted(initial_req)
    close = closest_to_head(head, initial_req)
    c = initial_req.index(close)
    if close >= head:
        requests_right = initial_req[c:]
        for each in requests_right:
            if each in initial_req:
                schedule.append(each)
                service_req.append(each)
                wait_time += abs(head - each)
                head = each
                initial_req.remove(each)
        if len(service_req) == number_of_req:
            return head, wait_time
        else:
            wait_time += diff1
            index = last
            head = last
            while (index >= 0):
                if index in initial_req:
                    schedule.append(index)
                    service_req.append(index)
                    wait_time += abs(head - index)
                    head = index
                    initial_req.remove(index)
                index = index - 1
            return head, wait_time
    else:
        requests_left = initial_req[:c+1]
        for i in reversed(requests_left):
             if i in initial_req:
                schedule.append(i)
                service_req.append(i)
                wait_time += abs(head - i)
                head = i
                initial_req.remove(i)
        if len(service_req) == number_of_req:
            return head, wait_time
        else:
            wait_time += diff2
            index = first
            head = first
            while (index <= last):
                if index in initial_req:
                    schedule.append(index)
                    service_req.append(index)
                    wait_time += abs(head - index)
                    head = index
                    initial_req.remove(index)
                    head = index
                index = index + 1
            return head, wait_time


if __name__ =='__main__':
    schedule = []
    range = 10
    first = 0
    last = 199
    input_file = open(sys.argv[1], 'r')
    head, requests = input_file.readlines()
    head = int(head)
    requests = requests.split(',')
    requests = [int(x) for x in requests]
    queue1, queue2 = [], []
    wait_time = 0
    if len(requests) <= range:
        queue1 = requests[:]
        head, wait_time = scan(head, queue1, first, last)
        print(','.join([str(x) for x in schedule]))
        print wait_time
        print str(schedule[len(schedule) - 1]) + "," + str(wait_time)
    else:
        queue1 = requests[:range]
        requests = requests[range:]
        while (queue1):
            result = scan(head, queue1, first, last)
            head = result[0]
            wait_time += result[1]
            if len(requests) <= range:
                del queue1
                queue1 = requests[:]
            else:
                del queue1
                queue1 = requests[:range]
            requests = requests[range:]
        print(','.join([str(x) for x in schedule]))
        print wait_time
        print str(schedule[len(schedule) - 1]) + "," + str(wait_time)
