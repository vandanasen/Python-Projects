#remove element
def merge_list():
    nums=[0,1,2,2,3,0,4,2]
    val=2
    newnums=[]
    for i in range(len(nums)):
        if nums[i] != val:
           newnums.append(nums[i])
    print(len(newnums))


merge_list()
def main():
     if __name__ == '__main__':
         main()