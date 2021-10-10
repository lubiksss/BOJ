n = 8
lost = [1, 3, 5]
reserve = [3, 4, 7]


have = [0] + [1] * (n)

n_reserve = set(reserve)-set(lost)
n_lost = set(lost)-set(reserve)

for i in n_lost:
    have[i] = 0

for i in n_reserve:
    if 1 <= i-1 and not have[i-1]:
        have[i-1] = 1
        continue

    if n >= i+1 and not have[i+1]:
        have[i+1] = 1
        continue

print(sum(have))
