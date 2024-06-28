class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        int cnt[n];
        memset(&cnt, 0, n * sizeof(int));

        for (int i = 0; i < roads.size(); i++) {
            cnt[roads[i][0]]++;
            cnt[roads[i][1]]++;
        }
        sort(cnt, cnt + n);

        long long output = 0;
        for (int i = n; i > 0 && cnt[i - 1] > 0; i--) {
            output += (long long) i * (long long) cnt[i - 1];
        }
        return output;
    }
};
