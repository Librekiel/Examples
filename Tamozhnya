N = int(input())
events = []
for i in range(N):
    T,L = map(int, input().split())
    events.append((T,1))
    events.append((T+L,-1))
    
events.sort()
goodsin = 0
maxgoodsin = 0
for T, t in events:
    if t == 1:
        goodsin += 1
    else:
        goodsin -= 1
    maxgoodsin = max(maxgoodsin, goodsin)

print(maxgoodsin)
