bool isPalindrome(char* s) {
    int left = 0;
    int right = 0;

    while (s[right + 1]) {
        right++;
    }

    while (left < right) {
        if (s[left] <= 90 && s[left] >= 65) {
            s[left] += 32;
        } else if (!((s[left] <= 57 && s[left] >= 48) || s[left] <= 122 && s[left] >= 97)) {
            left++;
            continue;
        }

        if (s[right] <= 90 && s[right] >= 65) {
            s[right] += 32;
        } else if (!((s[right] <= 57 && s[right] >= 48) || (s[right] <= 122 && s[right] >= 97))) {
            right--;
            continue;
        }
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
}