import sys
from typing import List
# For getting input
sys.stdin = open('a.txt', 'r')

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

    def addInDegree(self, st: int, t: int) -> None:
        stt = tuple(st, t)
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
        intersections[street_names[x[i]].B].addOutDegree(street_names[x[i]].getID())
        intersections[street_names[x[i]].E].addInDegree(street_names[x[i]].getID(), i)



def ret(I: list):
    for i in I:
        print(i)
        intersections[i].get
