class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let tmpArray = []
        for(let i=0; i<nums.length; i++){
            if(tmpArray.includes(nums[i])){
                return true;
            }
            tmpArray.push(nums[i]);
        }
        return false;
    }
}
