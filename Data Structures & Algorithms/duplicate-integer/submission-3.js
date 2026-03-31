class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let tmpSet = new Set();

        for(let i = 0; i < nums.length; i++){
            if(tmpSet.has(nums[i])) return true;
            else tmpSet.add(nums[i]);
        }
        return false;
    }
}
