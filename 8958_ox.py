def test(ox):
    oxscore = [0 for i in range(len(ox))]
    if ox[0] == 'O':
        oxscore[0] = 1
    for i in range(1,len(ox)):
        if ox[i] == 'X':
            oxscore[i] = 0
        elif ox[i] == ox[i-1]:
            oxscore[i] = oxscore[i-1]+1
        elif ox[i] == 'O':
            oxscore[i] = 1

    return oxscore

a = int(input())
for i in range(a):
    print(sum(test(input())))