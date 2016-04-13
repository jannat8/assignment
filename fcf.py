def main():
 data=[{"pn":"p1","at":0,"bt":24},{"pn":"p2","at":3,"bt":3},{"pn":"p3","at":4,"bt":4}];
 
 print "\n FCF \n"
 st=0
 wt=[0,0,0]
 i=0
 while i<3:
  wt[i]=st-data[i]["at"]
  print data[i]["pn"],"waiting time :",wt[i]
  st=data[i]["bt"]+st
  i=i+1
 print "\n The average waiting time: ",wt[0],"+",wt[1],"+",wt[2],"/ 3 =",((wt[0]+wt[1]+wt[2])/3)


if __name__=="__main__":
 main()
