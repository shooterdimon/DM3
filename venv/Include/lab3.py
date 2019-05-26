import math
import random
inf = math.inf
n=int(input("Please enter number of nodes"))
v=int(input("Start node`s index"))
v_end = int(input("Final node`s index"))
d = [ inf for i in range(n)]
d[v]=0
e = [{"first":random.randint(0,n-1),"second":random.randint(0,n-1),"value":random.randint(0,n-1)} for i in range(n)]#,{"first":0,"second":2,"value":3},{"first":1,"second":2,"value":1},{"first":0,"second":1,"value":2}]
for i in range(n):
     for j in range(len(e)):
        if d[e[j]["second"]]>d[e[j]["first"]]+e[j]["value"]:
            d[e[j]["second"]] = d[e[j]["first"]]+e[j]["value"]
        if d[e[j]["first"]]>d[e[j]["second"]]+e[j]["value"]:
            d[e[j]["first"]] = d[e[j]["second"]]+e[j]["value"]
print(e)
print(d)