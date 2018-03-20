Number = int(input())
i = 0
First_num = 0
Second_num = 1
while(i < Number):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_num + Second_num
                      First_num = Second_num
                      Second_num = Next
                     
           print([Next])
           i = i + 1
