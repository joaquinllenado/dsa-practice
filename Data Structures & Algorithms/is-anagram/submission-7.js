class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;

        let countS = {};
        let countT = {};

        for(let i in s){
            countS[s[i]] = 1 + (countS[s[i]] || 0);
            countT[t[i]] = 1 + (countT[t[i]] || 0);
        }

        for(let i in countS){
            if (countS[i] !== countT[i]) {
                return false;
            }
        }

        return true;
    }
}
