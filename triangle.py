#####################@ 杨辉三角  @###########################
#Generator、list 练习
def triangles():
    tempList,RowList=[1],[1]
    num,cnt=1,0
    while True:
        if cnt==0:
            cnt=cnt+1
            yield RowList
        elif cnt==1:
            cnt=cnt+1
            RowList.append(1)
            yield RowList
        else:
            ####方式1：#####通过深拷贝方式##############
            RowList.append(1)
            tempList=list(RowList)
            cnt=cnt+1
            i,num=0,cnt-2   #num是循环次数
            while i<num:
                RowList[i+1]=tempList[i]+tempList[i+1]
                i=i+1
            ############################################
            
            
            yield RowList
        
        
        #print(RowList)

    
result=[]
n=0
for t in triangles():
    print(t)
    result.append(t)
    n=n+1
    if n==12:
        break
#####################@ End of 杨辉三角 @##################
