class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStrings = []
        for string in strs:
            encodedStrings.append(f"{len(string)}#{string}")
        return "".join(encodedStrings)

    def decode(self, s: str) -> List[str]:
        if (len(s) == 0):
            return []
        
        decodedStrings = []
        num = None
        start = 0
        while (start < len(s)):
            sharp = s.index("#", start)
            num = int(s[start:sharp])
            decodedStrings.append(s[sharp + 1: sharp + 1 + num])
            start = sharp + 1 + num
        
        return decodedStrings
            
