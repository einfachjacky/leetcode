class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s=[_ for _ in s]
        s_long = []
        max_length=0
        for letter in s:
            if not letter in s_long:
                s_long.append(letter)
            else:
                s_long = s_long[s_long.index(letter)+1:]
                s_long.append(letter)
            if len(s_long)>max_length:
                max_length=len(s_long)
        return max_length
