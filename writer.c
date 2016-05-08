#include<stdio.h>
#include<stdlib.b>

int main()
{
 int readCount=0;
 int wcount=0;
 binary semaphore mutex=1;
 binary semaphore rdr=1;
 binary semaphore wrt=1;
 do{
     wait(rdr);
     printf("\nreading.............................");
     if(readCount>0) // if there are already readers
     {while(readCount!=0)
       { wait(mutex);
       readCount--;
       signal(mutex);}
      }
     signal(rdr);
    signal(wrt); // signal that "if wait wrt" in writer
    }while(1);

 do{
    wait(mutex);
    wcount++;
    if(rdr=0) //already readers
      {
        wait(wrt);// wait for them
      }
     if(wcount==1)
     { wait(rdr);
     }
    signal(mutex);
  
   
    wait(wrt); // onlyy one writer at a time

    printf("\n  writing ");
   wait(mutex);
   wcount--;
   if(wcount==0)
        signal(rdr);
    readCount++;
    signal(wrt);
    signal(mutex);
   
   
  }while(1);
 







}
