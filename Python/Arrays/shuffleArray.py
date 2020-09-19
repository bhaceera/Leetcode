# input: [x1,x2,x3,...xn,y1,y2,y3,...yn]
# output: [x1,y1,x2,y2,x3,y3,...xn,yn]
# n = number of elements for x an y i.e if x has 4 elements, so does y and n = 4
# len(nums) = 2n

def shuffle(nums, n):
        shuffled_list = []

        for i in range(n):
                shuffled_list.append(nums[i])
                shuffled_list.append(nums[n+i])
                
        return shuffled_list

arr =[2,5,1,3,4,7]
arr2 = [1,2,3,4,5,6,7,8]

print(shuffle(arr, 3))
print(shuffle(arr2, 4))


def shuffleFaster(nums, n: int):
        zipped = zip(nums[0:n], nums[n:2*n])
        result = []
        for i in zipped:
            result += i
        return result
        
print(shuffleFaster(arr, 3))
print(shuffleFaster(arr2, 4))
