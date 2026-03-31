class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let hash = {};

        for(const str of strs){
            let key = Array(26).fill(0);
            for(const ltr of str){
                key[ltr.charCodeAt(0) - 'a'.charCodeAt(0)]++;
            }
            if(!hash[key]){
                hash[key] = [];
            }
            
            hash[key].push(str);

        }
        return Object.values(hash);
    }
}
