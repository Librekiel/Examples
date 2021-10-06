f = open('input.txt')
ans = dict()

for line in f:
    words = line.split()
    for word in words:
        ans[word] = ans.get(word, 0) + 1

ans = map(lambda x: x[1], sorted(map(lambda x: (max(ans.values())-x[1],x[0]),ans.items())))
print(*ans, sep = '\n')
