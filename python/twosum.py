number_list = [-2,2,3,4,5,7,11,13]
target = 9

def twosumBruteForce(nums, target):
    """
    Brute for solution to the two sum question
    """
    for i in range(len(nums)-1): # Loop through each number as the outter loop
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return[nums[i] + nums[j]]