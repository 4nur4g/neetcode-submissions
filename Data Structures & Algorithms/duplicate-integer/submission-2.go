func hasDuplicate(nums []int) bool {
   my_set := make(map[int]struct{}) 
   for _,item := range nums {
        _, exists := my_set[item]
        if exists {
            return true
        }
        my_set[item] = struct{}{}
   }
   return false
}
