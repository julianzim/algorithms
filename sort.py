# O(n^2)
def selection_sort(_lst: list) -> list:
    lst = _lst.copy()
    N = len(lst)
    for i in range(N-1):
        m, p = lst[i], i
        for j in range(i+1, N):
            if lst[j] < m:
                m, p = lst[j], j
        lst[p], lst[i] = lst[i], lst[p]
    return lst

# O(n^2)
def insertion_sort(_lst: list) -> list:
    lst = _lst.copy()
    N = len(lst)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    return lst

# O(n^2)
def bubble_sort(_lst: list) -> list:
    lst = _lst.copy()
    ...
    return lst
