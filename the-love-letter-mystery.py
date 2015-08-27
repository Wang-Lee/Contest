n = int(input())
for _ in range(n):
    w = input()
    w = [ord(x) for x in w]
    lenght = len(w)-1
    dif = 0
    for i in range(len(w)):
        dif += abs(w[lenght-i] - w[i])
    print(dif//2)
    
