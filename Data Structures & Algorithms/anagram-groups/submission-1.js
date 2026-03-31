class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let hashMap = {};

        for (let str of strs){
            let key = new Array(26).fill(0);
            for(let ltr of str){
                let hex = ltr.charCodeAt(0) - "a".charCodeAt(0);
                key[hex]++;
            }

            if(!hashMap[key]) hashMap[key] = [];
            
            hashMap[key].push(str);
        }

        return Object.values(hashMap);
    }
}
