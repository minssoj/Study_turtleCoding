T = [73,74,75,71,69,72,76,73]
hotday = []
for i,j in enumerate(T):
    wait = 0
    for k,l in enumerate(T):
        if j < l and i < k:
            wait = k-i
            break
    hotday.append(wait)
print(hotday)