x = ['hello', '12358', '756', '!#:/','!','fg','whs']
t = 0
y = []
while t < len(x):
    if len(x[t]) <= 3:
        y.append(x[t])
        t += 1
    else:
        t += 1

print (y)