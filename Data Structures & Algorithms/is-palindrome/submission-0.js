class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let start = 0;
        let end = s.length - 1;

        while(start < end){
            while (start < end && !this.alphaNum(s[start])){
                start++;
            }
            while (end > start && !this.alphaNum(s[end])){
                end--;
            }
            if (s[start].toLowerCase() !== s[end].toLowerCase()) return false;
            start++;
            end--;
        }
        return true;
    }

    alphaNum(c) {
        const charCode = c.charCodeAt(0);
        return (
            (65 <= charCode && charCode <= 90) ||
            (97 <= charCode && charCode <= 122) ||
            (48 <= charCode && charCode <= 57)
        );
    }
}
