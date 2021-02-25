import sys
from typing import List
import math
# For getting input
sys.stdin = open('b.txt', 'r')
sys.stdout = open('b_output.txt', 'w')

input = lambda : sys.stdin.readline().strip()
print = lambda s, end='\n' : sys.stdout.write(str(s) + end)

D, I, S, V, F = map(int, input().split())

street_names = {}

class street:
    def __init__(self, name, B, E, L, ID) -> None:
        self.name = name
        self.B = B
        self.L = L
        self.E = E
        self.ID = ID
        self.cars = {}
    
    def getID(self) -> int:
        return self.ID

    def addCar(self, car) -> None:
        self.cars[car] = True

class intersection:
    def __init__(self, ID) -> None:
        self.ID = ID
        self.in_degree_total = {}
        self.out_degree = {}

    def addInDegree(self, st: str) -> None:
        if st not in self.in_degree_total:
            self.in_degree_total[st] = 1
        else:
            self.in_degree_total[st]+= 1

    def addOutDegree(self, st: int) -> None:
        if st not in self.out_degree:
            self.out_degree[st] = 1
        else:
            self.out_degree[st]+= 1

    def getSchedule(self, key) -> list:
        return [key, int(math.ceil(float(self.in_degree_total[key])/float(D)))]
        
    def getScheduleCount(self) -> int:
        return len(self.in_degree_total)

intersections = [intersection(i) for i in range(I)]

for i in range(S):
    x = input().split()
    B = int(x[0])
    E = int(x[1])
    name = x[2]
    L = int(x[3])
    street_names[name] = street(name, B, E, L, i)

for j in range(V):
    x = input().split()
    P = int(x[0])
    for i in range(1, P+1):
        street_names[x[i]].addCar(j)
        # intersections[street_names[x[i]].B].addOutDegree(x[i])
        intersections[street_names[x[i]].E].addInDegree(x[i])

# def ret(I: list):
#     print(len(I))
#     for i in I:
#         print(i)
#         l = intersections[i].getScheduleCount()
#         print(l)
#         for j in range(l):
#             sched = next(intersections[i].getSchedule())
#         intersections[street_names[x[i]].E].addInDegree(x[i], i)

def ret(QQ: list):
    print(len(QQ))
    for i in QQ:
        print(i)
        l = intersections[i].getScheduleCount()
        print(l)
        for key in intersections[i].in_degree_total:
            sched = intersections[i].getSchedule(key)
            stringz = str(sched[0]) + " " + str(sched[1])
            print(stringz)

# if __name__ == "__main__":
#     I = [i for i in ]
#     ret([0,1,2,3])        l = intersections[i].getScheduleCount()
#         print(l)
#         for j in range(l):
#             sched = next(intersections[i].getSchedule())
#             stringz = str(sched[0]) + " " + str(sched[1])
#             print(stringz)

if __name__ == "__main__":
    QQ = []
    for i in range(I):
        if len(intersections[i].in_degree_total) > 0:
           QQ.append(i)
    ret(QQ)
