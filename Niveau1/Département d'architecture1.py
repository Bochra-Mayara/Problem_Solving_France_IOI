n = int(input())

st = 0
i = 0
while st + (i*i)<=n:
    st += i*i
    i += 1
print(i-1)
print(st)