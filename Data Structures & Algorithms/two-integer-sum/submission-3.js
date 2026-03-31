class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hash = {};

        for (let i in nums){
            let diff = target - nums[i];
            if (hash[diff]){
                return [Number(hash[diff]), Number(i)];
            }
            hash[nums[i]] = i;
        }
    }
}

