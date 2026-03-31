class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let tmpSet = new Set();

        for(const num of nums){
            if(tmpSet.has(num)) return true;
            tmpSet.add(num);
        }
        return false;
    }
}
