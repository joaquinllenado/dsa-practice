class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hashmap = {};
        for(const i in nums){
            let diff = target - nums[i];
            if(hashmap[diff]) return([Number(hashmap[diff]), Number(i)]);
            hashmap[nums[i]] = i;
        }
    }
}
