from math import fabs

ans = []
currentInd = 0
n = int(input())
pairHome = []
home = list(map(int, input().split()))
m = int(input())
pairBomb = []
bombHouse = list(map(int, input().split()))
for i in range(n):
    tempData = (i + 1, home[i])
    pairHome.append(tempData)
for i in range(m):
    tempData2 = (i + 1, bombHouse[i])
    pairBomb.append(tempData2)
pairHome.sort(key=lambda x: x[1])
pairBomb.sort(key=lambda x: x[1])
k = len(pairBomb)
for i in range(n):
    for j in range(k):
        if k == 1:
            ans.append((pairHome[i][0], pairBomb[0][0]))
            break
        elif abs(pairBomb[0][1] - pairHome[i][1]) > \
                abs(pairBomb[1][1] - pairHome[i][1]):
            pairBomb.pop(0)
        elif abs(pairBomb[0][1] - pairHome[i][1]) == \
                abs(pairBomb[1][1] - pairHome[i][1]):
            ans.append((pairHome[i][0], min(pairBomb[0][0], pairBomb[1][0])))
            break
        else:
            ans.append((pairHome[i][0], pairBomb[0][0]))
            break
        k = len(pairBomb)
ans.sort()
for z in range(len(ans)):
    print(ans[z][1], end=' ')
