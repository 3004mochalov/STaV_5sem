def partition(arr, l, r):
    x = arr[r]
    less = l

    for i in range(l, r):
        if arr[i] <= x:
            arr[i], arr[less] = arr[less], arr[i]
            less += 1

    arr[less], arr[r] = arr[r], arr[less]
    return less


def q_sort_impl(arr, l, r):
    if l < r:
        q = partition(arr, l, r)
        q_sort_impl(arr, l, q-1)
        q_sort_impl(arr, q+1, r)
    return arr
        


def q_sort(arr):
    return q_sort_impl(arr, 0, len(arr)-1)


def merge_sort_impl(arr, buff, l, r, lvl):
    if l < r:
        m = int((l + r) / 2)
        merge_sort_impl(arr, buff, l, m, lvl+1)
        merge_sort_impl(arr, buff, m+1, r, lvl+1)

        k = l
        i, j = l, m + 1
        while i <= m or j <= r:
            if j > r or (i <= m and arr[i] < arr[j]):
                buff[k] = arr[i]
                i += 1
            else:
                buff[k] = arr[j]
                j += 1
            k += 1

        for i in range(l, r+1):
            arr[i] = buff[i]

    if lvl == 0:
        return arr


def merge_sort(arr):
    buff = [-1 for i in range(len(arr))]
    return merge_sort_impl(arr, buff, 0, len(arr)-1, 0)