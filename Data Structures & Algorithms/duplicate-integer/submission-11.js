class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const hashSet = new Set;

        for(const num of nums){
            if (hashSet.has(num)) return true;
            hashSet.add(num);
        }
        return false;
    }
}
