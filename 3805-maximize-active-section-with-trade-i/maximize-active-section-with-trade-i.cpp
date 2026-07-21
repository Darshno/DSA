class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        int ones = 0;
        for (char c : s)
            if (c == '1') ones++;

        // Augment with '1' at both ends.
        string t = "1" + s + "1";

        vector<pair<char, int>> seg;
        for (int i = 0; i < t.size();) {
            int j = i;
            while (j < t.size() && t[j] == t[i]) j++;
            seg.push_back({t[i], j - i});
            i = j;
        }

        int best = 0;

        // A removable 1-segment must have a 0-segment on both sides.
        for (int i = 1; i + 1 < seg.size(); i++) {
            if (seg[i].first == '1' &&
                seg[i - 1].first == '0' &&
                seg[i + 1].first == '0') {
                best = max(best, seg[i - 1].second + seg[i + 1].second);
            }
        }

        return ones + best;
    }
};