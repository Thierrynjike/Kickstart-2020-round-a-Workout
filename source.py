T = int(input())
out = []
for i in range(T):
    n, k = list(map(int, input().split()))
    session = list(map(int, input().split()))
    dif = [abs(session[i] - session[i + 1]) for i in range(len(session) - 1)]
    while (k != 0):
        ind = dif.index(max(dif))  # the index of the max difference
        session.insert(ind + 1, session[ind] + max(dif) // 2)
        # insert the middle value between the two relative value
        dif = [abs(session[i] - session[i + 1]) for i in range(len(session) - 1)]
        k -= 1

    out.append(max(dif))
for j in range(len(out)):
    print('Case #{}: {}'.format(j + 1, out[j]))