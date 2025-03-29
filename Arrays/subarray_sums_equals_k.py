from collections import defaultdict
def subarraySum(nums, k):
    n = len(nums)
    preSum,cnt =0,0
    mpp = defaultdict(int)
    mpp[0]=1
    for i in range(n):
        preSum+=nums[i]
        remove = preSum-k
        cnt += mpp[remove]
        mpp[preSum]+=1
    return cnt

if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = subarraySum(arr, k)
    print("The number of subarrays is:", cnt)