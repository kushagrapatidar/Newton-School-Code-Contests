N=int(input())
set=[]
for _ in range(N+1):
    set.append(int(input()))
set.sort()
subset=[]
for _ in set:
    if _//2 not in subset:
        subset.append(_)
print(len(subset))
for _ in subset:
    print(_)