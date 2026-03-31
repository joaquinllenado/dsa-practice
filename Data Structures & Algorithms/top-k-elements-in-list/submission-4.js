class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let count = {};
        let freq = Array.from({length: nums.length + 1}, () => []);

        for(let num of nums){
            count[num] = 1 + (count[num] || 0);
        }

        for(let i in count){
            freq[count[i]].push(Number(i));
        }

        let answer = [];

        for(let i = freq.length - 1; i > 0; i--){
            for(let j of freq[i]){
                answer.push(j);
                if(answer.length === k){
                    return answer;
            }
            }
            
        }
    }
}
