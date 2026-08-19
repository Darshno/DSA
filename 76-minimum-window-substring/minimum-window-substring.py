class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        char_count = defaultdict(int)
        for ch in t:
            char_count[ch] +=1
        
        tcr = len(t)
        min_win = (0,float("inf"))
        st = 0

        for end,ch in enumerate(s):
            if char_count[ch] > 0:
                tcr -= 1
            char_count[ch] -= 1
            if tcr == 0:
                while True:
                    cas = s[st]
                    if char_count[cas] == 0:
                        break
                    char_count[cas] += 1
                    st += 1
                if end - st < min_win[1] - min_win[0]:
                    min_win = (st,end)
                char_count[s[st]] += 1
                tcr +=1
                st += 1
        return "" if min_win[1] > len(s) else s[min_win[0]:min_win[1]+1]