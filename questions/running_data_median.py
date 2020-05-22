# Time series data of 24 hrs in 24 hr format
# Value is populated with random numbers
# Number of values for each interval can be different and unsorted
# return mean, median, mode of last x hrs or between x - y hrs


import random
import heapq
import csv


class analyzeData:
    def __init__(self,x,y,data):
        self.x = x
        self.y = y
        self.data = data
        self.max_heap = []
        self.min_heap = []
        self.mode_dict = {}
        self.max = -9999
        self.mode_elements = []
        self.sum = 0
        self.len_data = 0

        for i in range(len(self.data)):
            if(self.data[i][0] == x):
                while(self.data[i][0] < y):
                    #find mean
                    self.sum += self.data[i][1]
                    self.len_data += 1

                    #find median
                    self.insert_data(self.data[i][1])

                    #find mode
                    if(self.data[i][1] in self.mode_dict):
                        self.mode_dict[self.data[i][1]] += 1
                    else:
                        self.mode_dict[self.data[i][1]] = 1

                    if(self.mode_dict[self.data[i][1]] == self.max):
                        self.mode_elements.append(self.data[i][1])
                    elif(self.mode_dict[self.data[i][1]] > self.max):
                        self.mode_elements = [self.data[i][1]]
                        self.max = self.mode_dict[self.data[i][1]]
                    else:
                        pass

                    i += 1
                break



        median = self.find_median()
        mean = self.sum / self.len_data
        print("mean is {}\n".format(mean))
        print("median is {}\n".format(median))
        print("mode is {}\n".format(self.mode_elements))


    def insert_data(self,num):
        if(not self.max_heap and not self.min_heap):
            heapq.heappush(self.min_heap, num)
            return
        if(not self.max_heap):
            if(num > self.min_heap[0]):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
            return

        if len(self.max_heap) < len(self.min_heap):
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        elif len(self.max_heap) > len(self.min_heap):
            if num < -self.max_heap[0]:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if num < -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)


    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]




#generate random sample_data
sample_data = []
for k in range(25):
    if(k < 10 or k > 18):
        i = random.randint(1,10)
    else:   # number of data points for 10 AM to 6 PM are greater than remaining hrs
        i = random.randint(10,50)
    for l in range(i):
        j = random.randint(1,100)
        sample_data.append([k,j])

#write data in CSV to cross check
with open('sample_data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(sample_data)

# print(sample_data)


time1 = int(input("enter start time "))
while(time1 < 0 or time1 > 24):
    print("invalid time")
    time1 =  int(input("enter start time "))

time2 = int(input("enter end time "))
while(time2 < 0 or time2 > 24):
    print("invalid time")
    time2 =  int(input("enter end time "))
while(time2 == time1):
    print("start and end time is same")
    time2 =  int(input("enter end time "))
while(time1 > time2):
    print("start time {} hrs can not be greater than end time".format(time1))
    time2 =  int(input("enter end time "))

print("\n")

abc = analyzeData(time1,time2,sample_data)
