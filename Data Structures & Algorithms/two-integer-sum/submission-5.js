class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hash = {};

        for(const i in nums){
            let diff = target - nums[i];
            if(hash[diff]) return [Number(hash[diff]), Number(i)];
            hash[nums[i]] = i;
        }
    }
}
