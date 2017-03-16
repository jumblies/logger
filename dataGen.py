cell = [q for q in range(2,102)]
temp = [x/10 for x in range(1000, 900, -1)]
hum = [r/10 for r in range (900, 1000) ]
time = [y for y in range(2300, 2400)]
data = zip(time,temp)
data = [list(a) for a in zip(cell, time, temp, hum)]
print(data)
print(len(data))
