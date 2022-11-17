class Solution:
    def lengthOfLastWord(self,s):
         return len(s.split(" ")[-1])

s= Solution()
print(s.lengthOfLastWord(s="Hello my friend"))