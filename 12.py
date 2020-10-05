# number = [273,103,5,32,65,9,72,800,90]
# for el in number :
#     if el>=100:
#         print("100 이상의 수 : ",el)s

######################################

number = [1,2,3,4,5,6,7,8,9]
output=[]
#output = [[1,4,7],[2,5,8],[3,6,9]]
for i in number:
     output[(i+2)%3].append(i)
        
print(output)
   