class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) return false;

        const countS = {};
        const countT = {};
        for(const i in s){
            countS[s[i]] = 1 + (countS[s[i]] || 0);
            countT[t[i]] = 1 + (countT[t[i]] || 0);
        }

        for(const index in countS){
            if (countS[index] !== countT[index]) return false;
        }
        return true;
    }
}
