// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description/

char* maximumTime(char* time) {
    // Hours
    if (time[0] == '?' && time[1] == '?') {
        time[0] = '2';
        time[1] = '3';
    } else if (time[0] == '?') {
        if (time[1] - '0' <= 3) {
            time[0] = '2';
        } else {
            time[0] = '1';
        }
    } else if (time[1] == '?') {
        if (time[0] == '2') {
            time[1] = '3';
        } else {
            time[1] = '9';
        }
    }

    // Minutes
    if (time[3] == '?') {
        time[3] = '5';
    }
    if (time[4] == '?') {
        time[4] = '9';
    }

    return time;
}