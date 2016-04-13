def main():
 data=[{"pn":"p1","at":0,"bt":6},{"pn":"p2","at":0,"bt":8},{"pn":"p3","at":0,"bt":7}];
 print"\n SJF \n"
 
 sj=[0,0,0]
 if data[0]["bt"]<data[1]["bt"] :
    if data[0]["bt"]<data[2]["bt"] :
       sj[0]=0
       if data[1]["bt"]>data[2]["bt"]:
         sj[1]=2
         sj[2]=1
       else:
         sj[1]=1
         sj[2]=2
    else:
      sj[0]=2
      sj[1]=0
      sj[2]=1

 elif data[1]["bt"]<data[0]["bt"] :
    
   if data[1]["bt"]<data[2]["bt"]:
       sj[0]=1
       if data[0]["bt"]>data[2]["bt"]:
         sj[1]=2
         sj[2]=0
       else:
         sj[1]=0
         sj[2]=2
   else:
      sj[0]=2
      sj[1]=1
      sj[2]=0

 elif data[2]["bt"]<data[0]["bt"] :
    if data[2]["bt"]<data[1]["bt"] :
       sj[0]=2
       if data[0]["bt"]>data[1]["bt"]:
         sj[1]=1
         sj[2]=0
       else:
         sj[1]=0
         sj[2]=1
    else:
      sj[0]=1
      sj[1]=2
      sj[2]=0
 
 st=0
 wt=[0,0,0]
 i=0
 while i<3:
  wt[i]=st-data[sj[i]]["at"]
  print data[sj[i]]["pn"],"waiting time :",wt[i]
  st=data[sj[i]]["bt"]+st
  i=i+1
 print "\n The average waiting time: ",wt[0],"+",wt[1],"+",wt[2],"/ 3 =",((wt[0]+wt[1]+wt[2])/3)

 print"\n---------------------------------------\n"



if __name__=="__main__":
 main()
