arr=[]
arr=input()
def Remove(duplicate):
   
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
duplicate = arr
print(Remove(duplicate))
