import string
n = int(input())
lis = input().strip()
k = int(input())
k = k%26
p = re.compile(r'[a-zA-Z]')
res = []
for i in lis:
    if p.match(i):
        if i.islower():
            if ord(i) + k > 122:
                u = ord(i) + k - 122
                c = chr(96+u)
            else:
                c = chr(ord(i)+k)
           
        if i.isupper():
            if ord(i) + k > 90:
                u = ord(i) + k - 90
                c = chr(64+u)
            else:
                c = chr(ord(i)+k)
    else:
        c = i
    res.append(c)
print(''.join([str(x) for x in res]))
