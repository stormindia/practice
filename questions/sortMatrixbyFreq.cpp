// Sort a matrix in the following manner
// Store elements by the order of their frequency
// In case of a tie, priority should be given to the element having higher value
// Order of storing should be as follows - 
// start keeping the element from the bottom right index and store them diagonally 
//     9  8  6 
//     7  5  3   
//     4  2  1
// 1 represents the first element after sorting, 2 second element and so on

#include <iostream>
#include <vector>
#include <bits/stdc++.h> 
using namespace std; 

// matrix = []
// sorted_arr = []

//bool isValidIndex();
//void sortByFreq();

bool isValidIndex(int x,int y, vector <vector <int>> arr){
    if(x < 0 || x >= arr.size() || y < 0 || y >= arr[x].size()){
        return false;
    }
return true;
}

bool sortByVal(const pair<int, int>& a, const pair<int, int>& b) 
{ 
    // If frequency is same then sort by index 
    if (a.second == b.second)  
        return a.first < b.first; 
    return a.second > b.second; 
} 

// void sortByFreq(vector <int> sorted_arr) 
// { 
 
  
// }


// void sorted_array(int matrix[]){
// continue;
// }


int main(){
vector <vector <int>> arr { { 1, 2, 2, 1 }, 
                            { 4, 6, 4, 3 }, 
                            { -1, -2, -1, -2 }, 
                            {9, 0, 8, 1 } }; 
vector <int> sorted_arr;

for (int i = 0; i < arr.size(); i++) { 
    for (int j = 0; j < arr[i].size(); j++) { 
        //cout << arr[i][j] << " "; 
        //cout << endl;
        sorted_arr.push_back(arr[i][j]); 
    }
}

unordered_map<int, int> m; 
vector<pair<int, int> > v; 

for (int i = 0; i < sorted_arr.size(); ++i) { 

    // Map m is used to keep track of count  
    // of elements in array 
    m[sorted_arr[i]]++; 
}    

// Copy map to vector 
copy(m.begin(), m.end(), back_inserter(v)); 

// Sort the element of array by frequency 
sort(v.begin(), v.end(), sortByVal); 
static int k = 0;
for(int i = 0; i < v.size(); ++i){
    for (int j = 0; j < v[i].second; ++j){
        sorted_arr[k] = v[i].first;
        cout << v[i].first << endl;
        k += 1;
    }
}

for(int i = 0; i < sorted_arr.size(); i++){
   // cout<< sorted_arr[i] << endl;
}
return 0;

}