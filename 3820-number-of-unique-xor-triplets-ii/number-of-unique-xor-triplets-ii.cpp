class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        const int MAXX = 2048;   // nums[i] <= 1500, so XOR < 2048

        vector<bool> dp1(MAXX, false), dp2(MAXX, false), dp3(MAXX, false);

        for (int x : nums) {
            // Update dp3
            for (int v = 0; v < MAXX; v++) {
                if (dp2[v]) dp3[v ^ x] = true;
            }

            // Update dp2
            for (int v = 0; v < MAXX; v++) {
                if (dp1[v]) dp2[v ^ x] = true;
            }

            // Single element
            dp1[x] = true;
        }

        // Handle repeated indices (i = j or j = k)
        for (int x : nums) {
            dp2[0] = true;      // x ^ x
            dp3[x] = true;      // x ^ x ^ x
        }

        int ans = 0;
        for (bool ok : dp3)
            if (ok) ans++;

        return ans;
    }
};