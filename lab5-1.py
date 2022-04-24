from random import randrange

N = randrange(100)
array = []
for i in range(N):
    array.append(randrange(-100, 100))
print(array)

array_new = []
for i in array:
    if i < 0 and i % 2 == 1:
        array_new.append(i)
print(array_new)


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


mergeSort(array_new)
print(array_new)

j = 0
for i in range(N):
    if array[i] < 0 and array[i] % 2 == 1:
        array[i] = array_new[j]
        j += 1
print(array)
