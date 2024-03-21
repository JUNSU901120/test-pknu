hap, i = 0,0

for i in range(3333, 9999) :
    if i % 1234 == 0 :
        continue
    if hap+i > 100000 :
        break
    hap += i

print(hap)
