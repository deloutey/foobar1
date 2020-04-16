def solution(total_lambs):
    st = []
    gn = []
    while sum(gn) < 10 ** 9:
        if len(gn) == 0:
            gn.append(1)
        else:
            gn.append(gn[-1] * 2)
    while sum(st) < 10 ** 9:
        if len(st) == 0 or len(st) == 1:
            st.append(1)
        else:
            st.append(st[-2] + st[-1])
    for i in range(len(st)):
        if total_lambs < sum(st[:i + 1]):
            s = i
            break
    for i in range(len(gn)):
        if total_lambs < sum(gn[:i + 1]):
            g = i
            break
    return s - g
print(solution(10 ** 8))