class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=""
        for i in range(max(len(word1),len(word2))):
            print(i)
            if i<len(word1):
                print("entered")
                new+=word1[i]
                print(new)
            if i<len(word2):
                new+=word2[i]    
        return new    