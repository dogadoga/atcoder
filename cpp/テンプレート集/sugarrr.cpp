#include<atcoder/all>
#include<bits/stdc++.h>
 
using namespace std;
using namespace atcoder;
typedef long long ll;
 
typedef long double dd;
typedef pair<ll,ll> l_l;
typedef pair<dd,dd> d_d;
ll inf=(ll)1E18;
#define rep(i,l,r) for(ll i=l;i<=r;i++)
#define rrep(i,r,l) for(ll i=r;i>=l;i--)
#define pb push_back
ll max(ll a,ll b){if(a<b)return b;else return a;}
ll min(ll a,ll b){if(a>b)return b;else return a;}
dd EPS=1E-10;
#define fi first
#define se second
 
#define SORT(v) sort(v.begin(),v.end())
#define ERASE(v) sort(v.begin(),v.end()); v.erase(unique(v.begin(),v.end()),v.end())
#define POSL(v,x) (lower_bound(v.begin(),v.end(),x)-v.begin())
#define POSU(v,x) (upper_bound(v.begin(),v.end(),x)-v.begin())
template<class T,class S>
inline bool chmax(T &a, S b) {
    if(a < b) {
        a = (T)b;
        return true;
    }
    return false;
}
template<class T,class S>
inline bool chmin(T &a, S b) {
    if(a > b) {
        a = (T)b;
        return true;
    }
    return false;
}
#define all(c) c.begin(),c.end()
 
using mint = modint998244353;
//using mint = modint1000000007;
//using mint=modint;
//using mint=static_modint<100>;
//using mint=dd;
//using mint=ll;
 
 
typedef vector<mint>vi;
typedef vector<vi>vvi;
typedef vector<vvi>vvvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl>vvvl;
typedef vector<l_l>vl_l;
typedef vector<vl_l>vvl_l;
typedef vector<string>vs;
typedef vector<vs>vvs;
typedef vector<dd> vd;
typedef vector<vd> vvd;
typedef vector<d_d>vd_d;
dd PI=acos((dd)-1);
 
#define fastio ios::sync_with_stdio(false); cin.tie(0); cout.tie(0); cout<<fixed<<setprecision(18);
template <class T> using pq = priority_queue<T>;
template <class T> using pqg = priority_queue<T, vector<T>, greater<T>>;
 
// g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE main.cpp && ./a.out
#define endl "\n"  //インタラクティブで消す！！！！！！！！！！！！！！！！！！！！！
#define popcount __builtin_popcountll
#define SHUFFLE(v) shuffle(all(v),default_random_engine(chrono::system_clock::now().time_since_epoch().count()))
//////////////////////////
 
signed main(){fastio
    
    string s;cin>>s;
    while((int)s.size()<=3){
        s='0' + s;
    }
    cout<<s;
    
    return 0;
}