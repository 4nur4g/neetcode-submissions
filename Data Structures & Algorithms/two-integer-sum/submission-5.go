func twoSum(nums []int, target int) []int {
    track_map := make(map[int]int)
    for ind,n := range nums {
        diff := target - n
        val, exists := track_map[diff]
        if exists {
            return []int{val,ind}
        }
        track_map[n] = ind
    }
    return []int{}
}
