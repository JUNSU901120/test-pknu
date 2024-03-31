d_str = "파이썬 ### CookBook $$$ @@@ 열공중 1234"
m = " "

for i in range(len(d_str)):
    if d_str[i].isalpha():
        m+= d_str[i]

print(m)
