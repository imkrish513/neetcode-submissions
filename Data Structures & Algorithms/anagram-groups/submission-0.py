from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorted
        #hash map sorted ->og
        #append list
        sort = []
        for word in strs:
            sort.append("".join(sorted(word)))
        mp = defaultdict(list)

        for i in range(len(sort)):
            print(sort[i])
            mp[sort[i]].append(strs[i])
        fin = []
        for key,value in mp.items():
            fin.append(value)

        return fin


        

    
            
