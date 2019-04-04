dup_list = [0,0,0,0,1,2,3,4,4,4,5,6,7,7,7,8,9]

def remove_duplicates(nums):
    """
    Gives a count of the none duplicated charactors. Runs on (O)n
    """
    count = 1
    for i in range(1,len(nums)-1):
        if nums[i-1] == nums[i]:
        else:
            count += 1
    print(count)



remove_duplicates(dup_list)