def longestConsecutive(nums):
    n=len(nums)
    if n==0:
        return 0
    longest =1
    st = set()
    for i in range(n):
        st.add(nums[i])
    for it in st:
        if it-1 not in st:
            cnt =1
            x=it
            while x+1 in st:
                x+=1
                cnt+=1
            longest = max(longest,cnt)
    return longest

a = [100, 200, 1, 2, 3, 4]
ans = longestConsecutive(a)
print("The longest consecutive sequence is", ans)