class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const count = {};
        
        for(const str of strs){
            let freq = Array(26).fill(0);
            for(const ltr of str){
                freq[ltr.charCodeAt(0) - 'a'.charCodeAt(0)]++;
            }
            if (!count[freq]) count[freq] = [];
            count[freq].push(str);
        }

        return Object.values(count);
    }
}
