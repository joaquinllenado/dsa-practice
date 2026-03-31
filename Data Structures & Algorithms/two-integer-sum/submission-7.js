class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const hashMap = {};

        for(const i in nums){
            let diff = target - nums[i];
            if(hashMap[diff]){
                return [Number(hashMap[diff]), Number(i)];
            } 
            hashMap[nums[i]] = i;
        }
    }
}
