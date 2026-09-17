class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();

        // best[i] = minimum length of a valid subarray
        // completely within arr[0...i].
        vector<int> best(n, INT_MAX);

        int left = 0;
        long long sum = 0;
        int answer = INT_MAX;

        for (int right = 0; right < n; right++) {
            sum += arr[right];

            // Since all numbers are positive, shrink
            // the window while its sum is too large.
            while (left <= right && sum > target) {
                sum -= arr[left];
                left++;
            }

            // If current window has sum == target.
            if (sum == target) {
                int len = right - left + 1;

                // There must be a previous valid subarray
                // ending before 'left'.
                if (left > 0 && best[left - 1] != INT_MAX) {
                    answer = min(answer, len + best[left - 1]);
                }

                // Store the shortest valid subarray seen so far.
                if (right == 0) {
                    best[right] = len;
                } else {
                    best[right] = min(best[right - 1], len);
                }
            } else {
                // No valid subarray ending at 'right'.
                if (right > 0) {
                    best[right] = best[right - 1];
                }
            }
        }

        return answer == INT_MAX ? -1 : answer;
    }
};