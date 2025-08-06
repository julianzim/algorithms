
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
        Temporary array: O(n) | Recursion: O(log(n)) | In-place: O(1)
    '''
    lst = _lst
    ...
    return lst


def quick_sort(_lst: list) -> list:
    '''
    Time complexity:
        The worst: O(n^2) | Avg: O(n*log(n)) | The best: O(n*log(n))
    Space complexity:
        Imbalance split: O(n) | Recursion: O(log(n)) | In-place: O(1)
    '''
    lst = _lst
    ...
    return lst
