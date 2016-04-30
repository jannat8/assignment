#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<time.h>
void *MyThreadInitial(void *arg);
void *add(void *arg);
void *sub(void *arg);
void *display(void *arg);
pthread_mutex_t mut=PTHREAD_MUTEX_INITIALIZER;
int ans=0;
int main()
{
 
  int *status;
  int a1[100];
  pthread_t t1,t2,t3,t4;
  pthread_mutex_init(&mut,NULL);
  
  pthread_create(&t1,NULL,MyThreadInitial,(void*)&a1);
  pthread_join(t1,(void**)&a1);
  pthread_create(&t2,NULL,add,(void*)&a1);
  pthread_join(t2,NULL);
  pthread_create(&t3,NULL,sub,(void*)&a1);
   
  pthread_join(t3,NULL);
  pthread_create(&t4,NULL,display,(void*)&a1);
  pthread_join(t4,NULL);
  
  pthread_mutex_destroy(&mut);
  //printf("Sum value:  \n",param.s);
  return 0;
  }
void *MyThreadInitial(void *arg)
{
 int *a1=(int*)arg;
 int i=0;
 for(;i<100;i++)
  a1[i]=rand()%100+1;
 return ((void*)a1);
}
void*add(void *arg)
{
  int *a=(int*)arg;
  int i=0;
  
  for(;i<100;i++)
    {
    
       if(a[i]%2!=0)
         {
          pthread_mutex_lock(&mut);
           ans=a[i]*2+ans;
          pthread_mutex_unlock(&mut);
          // printf("\n add%i",ans);
         }
    }
   pthread_exit(NULL);
  
}
void*sub(void *arg)
{
  int *a=(int*)arg;
  int i=0;
 // printf("\n a%d",ans);
  for(;i<100;i++)
    {  
       if(a[i]%2==0)
        {
         pthread_mutex_lock(&mut);
         ans=ans-a[i];
         pthread_mutex_unlock(&mut);
       // printf("\n sub%i",ans);
         }
    }
   pthread_exit(NULL);
}
void*display(void *arg)
{
   printf("\n%d is answer " ,ans);
   pthread_exit(NULL);
}
