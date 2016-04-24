def main():
 
  time=0
  flag=0
  wait_time=0
  turnaround_time=0
  at=[0,1,2,3]
  bt=[9,5,3,4]
  rt=[9,5,3,4]
  np=4
  q=5
  n=4
  i=0
  j=0
  
  while np!=0:
  
   if rt[i]<=q and rt[i]>0:
    time =time+rt[i]
    rt[i]=0
    flag=1
       
   elif rt[i]>0:
    rt[i]=rt[i]-q
    time=time+q
      
   if rt[i]==0 and flag==1:
    np=np-1
    j=j+1
    print "\nP",j,") waiting time :" ,time-at[i]," And TAT :",time-at[i]-bt[i]
    wait_time=wait_time+time-at[i]-bt[i]
    turnaround_time=turnaround_time+time-at[i]
    flag=0
       
   if i==(n-1):
    i=0; 
   elif at[i+1]<=time:
    i=i+1
   else: 
    i=0 
   
  print "\nAverage Waiting Time =",(wait_time*1.0/n)
  print "\nAvg Turnaround Time = ",(turnaround_time*1.0/n) 
  
   
if  __name__== "__main__":
 main()
