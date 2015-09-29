# Enter your code here. Read input from STDIN. Print output to STDOUT
main=str(input())
sub=str(input())
occ=0
for i in range(len(main)):
    if sub[0]==main[i]:
        flag=0
        i=i+1
        if i<len(main):
            for j in range(1,len(sub)):
                if i<len(main):
                    if sub[j]==main[i]:
                        flag=1
                        i=i+1
                    else:
                        flag=0             

                else:
                    flag=0
        if flag==1:
            occ=occ+1
print (occ)
