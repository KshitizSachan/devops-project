#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int> temp(5, 0);
    for(int i=0 ; i<5 ; i++){
        temp[i] = i+1;
    }
    for(int i=0 ; i<5 ; i++){
        cout<<temp[i]<<" ";
    }
    return 0;
}