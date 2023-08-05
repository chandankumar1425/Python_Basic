##1
data = [("John", 25), ("Jane", 30)]
output = [f"{name} is {age} years old." for name, age in data]
output = " ".join(output)
print(output)

##2




##3
def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)
