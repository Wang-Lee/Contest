#  Service Lane Function
def lane_width():
    n,t = input().split()
    n,t = int(n),int(t)
    lane = [int(x) for x in input().split()]
    for i in range(t):
        i,j = input().split()
        i,j = int(i),int(j)
        print(min(lane[i:j+1]))
if __name__ == '__main__':
    lane_width()
