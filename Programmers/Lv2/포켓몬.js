// 0706 Solve
function solution(nums) {
    const nums_set = new Set(nums);
    if (nums_set.size >= parseInt(nums.length / 2)) return parseInt(nums.length / 2); else return nums_set.size;
}