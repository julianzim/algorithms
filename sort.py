# O(n^2)
def selection_sort(lst: list) -> list:
    N = len(lst)
    for i in range(N-1):
        m = lst[i]
        p = i
        for j in range(i+1, N):
            if lst[j] < m:
                m = lst[j]
                p = j
        lst[p] = lst[i]
        lst[i] = m
    return lst


