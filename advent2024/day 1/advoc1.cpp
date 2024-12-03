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
    sort(v1.begin(),v1.end()); // sorting the two vector!
    sort(v2.begin(),v2.end());
   
    int result = Advent_of_Code(v1,v2); // passing the sorted vectors!
    cout<<"[*] The Result is : "<< result;
    f.close();
    return 0;
}


int Advent_of_Code(vector<int>v1,vector<int>v2){
    
    vector<pair<int,int>> v3;
    pair<int,int>p;
    int result = 0;
    for(int i=0;i < v1.size() ;i++){
        p.first = v1[i];
        p.second = v2[i];
        v3.push_back(p); // pushing the pair back in the vector v3
    }
    for(int i=0 ; i<v3.size();i++){
        result += abs(v3[i].first - v3[i].second); // substracting the distance between the points and taking abs 
    }
    return result;
}