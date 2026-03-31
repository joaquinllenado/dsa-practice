class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let ans = {};

        for (let str of strs){
            let key = new Array(26).fill(0);
            for (let ltr of str){
                key[ltr.charCodeAt(0) - 'a'.charCodeAt(0)]++;
            }

            if(!ans[key]){
                ans[key] = [];
            }
            
            ans[key].push(str);
        }

        return Object.values(ans);

    }
}
