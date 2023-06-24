import math
n, m, a = map(int, input().split())

x = math.ceil(m/a)
x2 = math.ceil(n/a)

res=x*x2
print(res)

#Math.ceil para redondear al numero mas alto