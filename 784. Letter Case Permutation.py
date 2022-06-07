class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        finRes = []
        def helper(Out, In):
            if(In == ""):
                finRes.append(Out)
                return
            if(In[0].isnumeric()):
                helper(Out+In[0], In[1:])
            else:
                helper(Out+In[0].lower(), In[1:])
                helper(Out+In[0].upper(), In[1:])

        helper("", s)
        return finRes
