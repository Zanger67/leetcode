function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    let indx = 0;
    let counter = 0;
    while (indx < flowerbed.length) {
        if (flowerbed[indx] == 1)
            indx += 2;
        else if (indx > 0 && flowerbed[indx - 1] == 1)
            indx += 1;
        else if (indx < flowerbed.length - 1 && flowerbed[indx + 1] == 1)
            indx += 3;
        else {
            counter++;
            indx += 2;
        }

        if (counter >= n)
            return true;
    }

    return false;
};