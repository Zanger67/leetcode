impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        let mut indx = 0;
        let mut counter = 0;
        while (indx < flowerbed.len()) {
            if (flowerbed[indx] == 1) {
                indx += 2;
            }
            else if (indx > 0 && flowerbed[indx - 1] == 1) {
                indx += 1;
            }
            else if (indx < flowerbed.len() - 1 && flowerbed[indx + 1] == 1) {
                indx += 3;
            }
            else {
                counter += 1;
                indx += 2;
            }

            if (counter >= n) {
                return true;
            }
        }

        return false;
    }
}