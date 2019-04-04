number_list = [-2,2,3,4,5,7,11,13]
target = 9

def twosum_brute_force(nums, target):
    """
    Brute for solution to the two sum question this runs in (O)n^2 for worst case time with (O)1 on space
    """
    for i in range(len(nums)-1): # Loop through each number as the outter loop
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return[nums[i] + nums[j]]

def twosum_dictionary(nums, target):
    """
    This method keeps everythin in (O)n for time but does make space in the from of a dictionary
    """
    num_lookup = {}
    for i in range(len(nums)):
        if nums[i] in num_lookup:
            print([,])
        else:
