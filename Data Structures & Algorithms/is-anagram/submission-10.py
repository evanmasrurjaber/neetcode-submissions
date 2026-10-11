class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.create_dict(s)
        t_dict = self.create_dict(t)
        for i,j in s_dict.items():
            if i in t_dict and t_dict[i] == j:
                pass
            else:
                return False
        for i,j in t_dict.items():
            if i in s_dict and s_dict[i] == j:
                pass
            else:
                return False       
        return True

    def create_dict(self, s):
        val = {}
        for i in s:
            if i in val:
                val[i]+=1
            else:
                val[i] = 1
        return val