func flowerGame(n int, m int) int64 {
    return int64((n + 1) / 2) * int64(m / 2) + int64(n / 2) * int64((m + 1) / 2)
}