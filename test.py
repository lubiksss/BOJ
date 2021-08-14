import numpy
visited = [[0]*(3) for __ in range(3)]
for i in range(3):
    for j in range(3):
        visited[i][j] = []


print(visited)

visited[0][0].append(1)

print(id(visited[0][0]))
print(id(visited[0][1]))

print(visited)
