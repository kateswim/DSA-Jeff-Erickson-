def merge_sort(array):
    if len(array) < 1:
        return array
    else:
        mid=len(array)//2
        merge_sort(array[:mid])
        merge_sort(array[mid:])


def merge(array,mid):
    i=1
    j=mid+1
    for k in range(len(array)):
        if j > len(array):
            array[k]=array[i]
            i+=1
        elif i>mid:
            array[k]=array[j]
            j+=1
        elif array[i]<array[j]:
            array[k]=array[i]
            i+=1
        else:
            array[k]=array[j]
            j+=1

print(merge_sort([3,2,1,4,5,6,7,8,9,10]))    