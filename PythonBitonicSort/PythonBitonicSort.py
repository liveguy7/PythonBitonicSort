import sys

def compandSwap(a,i,j,dire):
    if(dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

def bitonicMerge(a,low,cnt,dire):
    if(cnt > 1):
        k = int(cnt / 2)
        for i in range(low, low + k):
            compandSwap(a,i,i+k,dire)
        bitonicMerge(a,low,k,dire)
        bitonicMerge(a,low+k,k,dire)

def bitonicSort(a,low,cnt,dire):
    if(cnt > 1):
        k = int(cnt / 2)
        bitonicSort(a,low,k,1)
        bitonicSort(a,low+k,k,0)
        bitonicMerge(a,low,cnt,dire)

def sort(a,N,up):
    bitonicSort(a,0,N,up)


def gnome_sort(nums):
    if(len(nums) <= 1):
        return nums

    i = 1
    while(i < len(nums)):
        if(nums[i-1] <= nums[i]):
            i = i + 1
        else:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            i = i - 1
            if(i == 0):
                i = 1

input1 = input("Enter: ").strip()
nums = [int(item) for item in input1.split(",")]
gnome_sort(nums)
for i in range(len(nums)):
    print(nums[i], end=' ')

def cocktail_shaker_sort(nums):
    for i in range(len(nums)-1,0,-1):
        is_swapped = False
        for j in range(i,0,-1):
            if(nums[j] < nums[j-1]):
                nums[j],nums[j-1] = nums[j-1], nums[j]
                is_swapped = True
        for j in range(i):
            if(nums[j] > nums[j+1]):
                nums[j],nums[j+1] = nums[j+1],nums[j]
                is_swapped = True
        if(not is_swapped):
            return nums

num1 = input('Input comma separated numbers:\n').strip()
nums = [int(i) for i in num1.split(",")]
print(cocktail_shaker_sort(nums))





















