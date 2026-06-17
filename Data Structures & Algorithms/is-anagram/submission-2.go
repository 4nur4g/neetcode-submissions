import "maps"

func isAnagram(s string, t string) bool {
    count_map_s := make(map[rune]int)
    count_map_t := make(map[rune]int)
    for _,c := range s {
        count_map_s[c] += 1
    }
    for _,c := range t {
        count_map_t[c] += 1
    }
    return maps.Equal(count_map_s,count_map_t)
}
