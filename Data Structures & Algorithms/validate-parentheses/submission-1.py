class Solution:
    def isValid(self, s: str) -> bool:
        validBrackets = {')':'(', '}':'{', ']':'['}
        valid = []
        
        for char in s:
            if char in validBrackets:
                if valid and valid[-1] == validBrackets[char]:
                    valid.pop()
                else:
                    return False
            else:
                valid.append(char)
        return True if not valid else False





