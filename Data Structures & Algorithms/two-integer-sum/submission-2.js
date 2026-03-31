class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let hashMap = {};

        for (let i in nums){
            let diff = target - nums[i];
            if (hashMap[diff]){
                return [Number(hashMap[diff]), Number(i)]
            }

            hashMap[nums[i]] = i;
        }
    }
}
