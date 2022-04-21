// 入力

// 単純な入出力
#include<bits/stdc++.h>
using namespace std;
int main(void){
    string s;
    cin>>s;
    cout<<s<<endl;
    return 0;
}

// 1行を配列に
#include <iostream>
#include <vector> //可変長配列
using namespace std;
int main()
{
    int n , j;
    cin>>n;
    vector<int> input(n); //int型のinputという名前の変数を要素数nで宣言
    for (int i=0;i<n;i++)
    {
        cin>>j;
        input[i]=j;
        cout<<input[i]<<endl;
    }
}


// 出力