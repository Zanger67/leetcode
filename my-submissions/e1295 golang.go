
import "strconv"
func findNumbers(nums []int) int {
    output := 0
    for _, n := range nums {
        n_str := strconv.Itoa(n)
        if len(n_str) % 2 == 0 {
            output++
        }
    }
    return output
}