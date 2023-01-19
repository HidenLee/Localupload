#https://mygumi.tistory.com/308
def quick_sort(target,left,right):
    def compareparts(target,left,right):
        low = left + 1 # 1
        high = right # 4
        pivot = target[left] #1
        while low < high:
            while low < right and target[low]<pivot:
                low += 1
            while high > left and target[high]>pivot:
                high -= 1    
            if low<high:
                target[low], target[high] = target[high], target[low]
        target[left], target[high] = target[high], target[left]
        return high
    
    if(left<right):
        pivotindex = compareparts(target,left,right)
        quick_sort(target, left, pivotindex-1)
        quick_sort(target, pivotindex+1, right)
num_list = [1,54,888,22,154,472,321,342,563,132,634,632]
quick_sort(num_list,0,len(num_list)-1)

print(num_list)
