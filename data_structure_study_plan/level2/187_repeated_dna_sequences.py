# URL: https://leetcode.com/problems/repeated-dna-sequences/

# 187. Repeated DNA Sequences

# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
 

# Constraints:

# 1 <= s.length <= 10**5
# s[i] is either 'A', 'C', 'G', or 'T'.


from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s)< 10:
            return []
        
        occurance= defaultdict(int)
        
        head= 0
        tail= 9
        
        while tail< len(s):
            occurance[s[head:tail+1]] += 1
            tail+=1
            head+= 1
        
        result= []
        for k,v in occurance.items():
            if v>1:
                result.append(k)
            
        return result