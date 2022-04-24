from random import randrange


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        _i = 0
        _j = 0
        _k = 0

        while _i < len(left_half) and _j < len(right_half):
            if left_half[_i] < right_half[_j]:
                alist[_k] = left_half[_i]
                _i = _i + 1
            else:
                alist[_k] = right_half[_j]
                _j = _j + 1
            _k = _k + 1

        while _i < len(left_half):
            alist[_k] = left_half[_i]
            _i = _i + 1
            _k = _k + 1

        while _j < len(right_half):
            alist[_k] = right_half[_j]
            _j = _j + 1
            _k = _k + 1


N = randrange(100)
array = []
for _ in range(N):
    array.append(randrange(-100, 100))
print(array)

array_new = []
for el in array:
    if el < 0 and el % 2 == 1:
        array_new.append(el)
print(array_new)


merge_sort(array_new)
print(array_new)

j = 0
for i in range(N):
    if array[i] < 0 and array[i] % 2 == 1:
        array[i] = array_new[j]
        j += 1
print(array)
