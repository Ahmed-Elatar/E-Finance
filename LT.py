
def solve(str1, str2):
    # Write your code here
    n = len(str2)
    c=''
    ans=[]
    flag=0
    for i in range(0,n):
        if str1[i] != str2[i]:
            ans.append(i)
            c=str1[i]
            flag=1
            break
    if flag == 0:
        ans.append(n)
        c=str1[-1]
    for i in range(ans[0]+1,n+1):
        if str1[i] == c:
            ans.append(i)
        else:
            break
    for i in range(ans[0]-1,0,-1):
        if str1[i] == c:
            ans.append(i)
        else:
            break
     
    return sorted(ans)
            



str1 = "aabbb"

str2 = "aabb"
print(solve(str1,str2))



# mmgghh
# mfggh


# ////



# aabbb
# aabb