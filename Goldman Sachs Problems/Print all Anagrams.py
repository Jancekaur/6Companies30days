

class Solution:
    def Anagrams(self, words, n):
        d=dict()
        for i in words:
            j=sorted(i)
            word="".join(j)
            if word in d.keys():
                d[word].append(i)
            else:
                d[word]=[i]
          
        l=[]  
        for x in d.keys():
            l.append(d[x])
            
        return l            
            

if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()
