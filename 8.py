i=1234
sum = 0

while i <= 4567:
    i+=1
    if i % 444 == 0:
        sum = sum + i

print('1234부터 4567 사이의 모든 444 배수의 합은 %d입니다.' %sum)
