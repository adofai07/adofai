import matplotlib.pyplot as P

f = open("C:/SSHS/codes/Research2.txt", "r")
data = f.readlines()
f.close()

for i in range(len(data)):
    data[i] = list(map(int, data[i].split()))

print(data)

x, y = [], []

for i in data:
    x.append(i[0])
    y.append(i[1])

P.plot(x, y)
P.show()