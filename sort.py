
def selection_sort(_lst: list) -> list:
    '''
    Time complexity:
        The worst: O(n^2) | The best: O(n^2)
    Space complexity:
        O(1) (if in-place)
    '''
    lst = _lst.copy()
    N = len(lst)
    for i in range(N-1):
        m, p = lst[i], i
        for j in range(i+1, N):
            if lst[j] < m:
                m, p = lst[j], j
        lst[p], lst[i] = lst[i], lst[p]
    return lst


def insertion_sort(_lst: list) -> list:
    '''
    Time complexity:
        The worst: O(n^2) | The best: O(n) (if already sorted)
    Space complexity:
        O(1) (if in-place)
    '''
    lst = _lst.copy()
    N = len(lst)
    for i in range(1, N):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    return lst


def bubble_sort(_lst: list) -> list:
    '''
    Time complexity:
        The worst: O(n^2) | The best: O(n) (if already sorted)
    Space complexity:
        O(1) (if in-place)
    '''
    lst = _lst.copy()
    N = len(lst)
    for i in range(N-1):
        for j in range(N-1-i):
            if lst[j+1] < lst[j]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst


def merge_sort(_lst: list) -> list:
    '''
    Time complexity:
        The worst: O(n*log(n)) | Avg: O(n*log(n)) | The best: O(n*log(n))
    Space complexity:
        O(n) (additional array)
    '''
    def merge_sorted_lists(a: list, b: list) -> list:
        res = []
        N, M = len(a), len(b)
        i = j = 0
        while i < N and j < M:
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        res.extend(a[i:] + b[j:])
        return res

    lst = _lst
    mid = len(lst) // 2
    lst_left, lst_right = lst[:mid], lst[mid:]

    if len(lst_left) > 1:
        lst_left = merge_sort(lst_left)
    if len(lst_right) > 1:
        lst_right = merge_sort(lst_right)

    return merge_sorted_lists(lst_left, lst_right)


def quick_sort(_lst: list) -> list:
    '''
    Time complexity:
        The worst: O(n^2) | Avg: O(n*log(n)) | The best: O(n*log(n))
    Space complexity:
        O(log(n)) (recursion)
    '''
    lst = _lst
    ...
    return lst
