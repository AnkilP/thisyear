import sys
from typing import List
import math
# For getting input
sys.stdin = open('a.txt', 'r')
sys.stdout = open('a_output.txt', 'w')

input = lambda : sys.stdin.readline().strip()
print = lambda s, end='\n' : sys.stdout.write(str(s) + end)

x = list(map(int, input().split(" ")))
D = x[0]
I = x[1]
S = x[2]
V = x[3]
F = x[4]

street_names = {}
intersections = []

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
        self.in_degree = {}
        self.in_degree_total = {}
        self.out_degree = {}

    def addInDegree(self, st: str, t: int) -> None:
        stt = tuple((st, t))
        if stt not in self.in_degree:
            self.in_degree[stt] = 1
            self.in_degree_total[st] = 1
        else:
            self.in_degree[stt]+= 1
            self.in_degree_total[st]+= 1

    def addOutDegree(self, st: int) -> None:
        if st not in self.out_degree:
            self.out_degree[st] = 1
        else:
            self.out_degree[st]+= 1

    def getSchedule(self) -> list:
        for key in self.in_degree_total:
            yield [key, int(math.ceil(float(self.in_degree_total[key])/float(D)))]
    
    def getScheduleCount(self) -> int:
        return len(self.in_degree_total)

for i in range(I):
    intersections.append(intersection(i))

for i in range(S):
    x = input().split(" ")
    B = int(x[0])
    E = int(x[1])
    name = x[2]
    L = int(x[3])
    street_names[name] = street(name, B, E, L, i)

for j in range(V):
    x = input().split(" ")
    P = int(x[0])
    for i in range(1, P+1):
        street_names[x[i]].addCar(j)
        intersections[street_names[x[i]].B].addOutDegree(x[i])
        intersections[street_names[x[i]].E].addInDegree(x[i], i)

def ret(I: list):
    print(len(I))
    for i in I:
        print(i)
        l = intersections[i].getScheduleCount()
        print(l)
        for j in range(l):
            sched = next(intersections[i].getSchedule())
            print(sched)
            stringz = str(sched[0]) + " " + str(sched(l[1]))
            print(stringz)


if __name__ == "__main__":
    ret([0,1,2,3])