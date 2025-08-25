func findDiagonalOrder(mat [][]int) []int {
    var output []int
    dirr := 1
    i, j := 0, 0

    for i < len(mat) && j < len(mat[0]) {
        output = append(output, mat[i][j])

        a, b := i - dirr, j + dirr

        if (0 <= a && a < len(mat)) && (0 <= b && b < len(mat[0])) {
            i = a
            j = b
            continue
        }

        if dirr == 1 {
            if j + 1 < len(mat[0]) {
                j += 1
            } else {
                i += 1
            }
            dirr *= -1
            continue
        }

        if i + 1 < len(mat) {
            i += 1
        } else {
            j += 1
        }
        dirr *= -1
    }

    return output
}