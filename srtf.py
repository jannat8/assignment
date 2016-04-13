def main():
 data=[{"pn":"p1","at":0,"bt":8},{"pn":"p2","at":3,"bt":10}];
 print "\n SRTF \n"


 run=[0,0,0]
 t=0
 i=0
 a=data[i]["at"]
 dur1=data[i]["bt"]
 dur2=data[i+1]["bt"]
 while a<data[i+1]["at"] :
  run[i]=t+1
  t=t+1
  dur1=dur1-1
  a=a+1
 while dur1!=0 and dur2!=0 :
  if dur1<dur2 and dur1!=0 or dur2==0:
   while dur1<dur2 and dur1!=0 or dur2==0:
    run[i]=t+1
    t=t+1
    dur1=dur1-1
  elif dur2<1 :
   while dur2<dur1 and dur2!=0 :
    run[i+1]=t+1
    t=t+1
    dur2=dur2-1
  
  
  st=0
 wt=[0,0]
 i=0
 while i<2:
  wt[i]=st-run[i+1]-data[i]["at"]
  print data[i]["pn"],"waiting time :",wt[i]
  st=data[i]["bt"]+st
  i=i+1
 print "\n The average waiting time: ",wt[0],"+",wt[1],"/ 2 =",((wt[0]+wt[1])/2)



 
if __name__=="__main__":
 main()
