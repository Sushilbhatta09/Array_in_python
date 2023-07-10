arr=[1,2,3,4]
s=11
n=4
start = 0
sum = arr[0]
for i in range(1,n+1):
    if sum == s:
        print( start+1, i)
        break
    elif i>n and sum<s:
        print("Not Found")
        break
    elif sum < s:
        sum=sum+arr[i]
        print("hekk",sum)
    elif sum>s:
        sum = sum - arr[start]
        start +=1
