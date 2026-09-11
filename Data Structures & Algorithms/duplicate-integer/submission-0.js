class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let setnums = new Set(nums);

        if(setnums.size == nums.length) {
            return false;
        }
        return true;
    }
}
