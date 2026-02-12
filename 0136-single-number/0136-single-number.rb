# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    -(nums.sum - nums.uniq.sum - nums.uniq.sum)
end