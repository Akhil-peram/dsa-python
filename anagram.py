def isAnagram(self, s: str, t: str) -> bool:
        so = sorted(s)
        to = sorted(t)
        if so == to:
            return True
        else:
            return False
        
