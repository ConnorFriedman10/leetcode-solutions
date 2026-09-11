class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const numMap = {}
        for (let num of nums) {
            if (!numMap[num]) {
                numMap[num] = 0;
            }
            numMap[num] += 1;
        }
        const result = Object.entries(numMap)
            .sort((a, b) => b[1] - a[1])
            .slice(0, k)
            .map(entry => Number(entry[0]));
        return result;
    }
}
