arr=[1,2,3,5,4]
is_sorted=True
for i in range(len(arr)-1):          #for i in range(1,len(arr)):
    if arr[i]>arr[i+1]:              #if arr[i]<=arr[i-1]:
        is_sorted=False
        break
if is_sorted:
    print("True")
else:
    print("False")