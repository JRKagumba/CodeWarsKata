#include <vector>
#include <bits/stdc++.h>

using namespace std;

int maxSequence(const vector<int>& arr){

  int sum=INT_MIN, holder=0, a = 0;
  
  if (arr.empty()==true)   //check for empty case
    return 0;
  
    for (int x : arr)
    {
      if (x > 0) //all negative or 0 case 
        a++;       //counting number of positive integers
    }
    
    
    if( a == 0) 
      return 0;
    else //kadane's algorithm
      for (int x : arr)
      {
      holder += x;
      sum = max(holder, sum);
      holder = max(holder,0);
      }
    
    return sum;
}