func findClosest(x int, y int, z int) int {
    a, b := x - z, y - z
    if a < 0 {
        a *= -1
    }
    if b < 0 {
        b *= -1
    }

    if a == b {
        return 0
    }
    if a < b {
        return 1
    }
    return 2
}