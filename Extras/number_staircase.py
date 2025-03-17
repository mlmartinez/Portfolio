'''
Makes a stair case out of numbers. Example: [[1]]   [[2][3]]    [[4][5][6]]
If the last stair is not longer than the previous one, the whole thing will
return as False.
'''
def main():
    '''provides the numbers for the staircase.'''
    nums = [1, 2, 3, 4, 5, 6]
    print(create_staircase(nums))

def create_staircase(nums):
    """makes the staircase"""
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets

if __name__ == "__main__":
    main()
