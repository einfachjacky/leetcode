class Solution:
    def reverseWords(self, s: str) -> str:
        wordlist = s.split(' ')
        wordlist = [i for i in wordlist if len(i)>0]
        return ' '.join(wordlist[::-1])
