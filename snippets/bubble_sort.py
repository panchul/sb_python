# bubble sort

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                
nums_list = [7,5,4,2,8,6,4,5]
print(nums_list)
sort(nums_list)
print(nums_list)