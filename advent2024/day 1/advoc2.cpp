#include<iostream>
#include<bits/stdc++.h>
#include<algorithm>

using namespace std;
int Advent_of_Code(vector<int>,vector<int>);

int main(){
    vector<int> v1;
    vector<int> v2;
    ifstream  f("text1.txt"); // Opening File 

    if(!f.is_open()){
        cout<<"[*] FIle Not Found!"<<endl; // Checking Error while Opening
    }

    string s ;
    while(getline(f,s)){
       istringstream iss(s); //  treat the line as a stream and extract integers
       int firstNumber , SecondNumber;

       if(iss >> firstNumber >> SecondNumber){
        v1.push_back(firstNumber);
        v2.push_back(SecondNumber);
       }else{
        cout<< "[*] Error Parsing Line!"<<endl;
       }
    }
    
    int result = Advent_of_Code(v1,v2); // passing the vectors!
    cout<<"[*] The Result is : "<< result;
    f.close();
    return 0;
}


int Advent_of_Code(vector<int>v1,vector<int>v2){

    int result = 0;
    unordered_map<int,int> m;

    // setting all the frequency of the elements to Zero! 
    for(auto i : v1){
      m[i] = 0;      
    }

    
    for(auto i : v2){
        if(find(v1.begin(), v1.end(),i) != v1.end()){
            m[i] += 1;
        }
    }
    
    for(auto i :v1){
       auto it = m.find(i);
       result += it->first * it->second;
    }
    return result;
}

