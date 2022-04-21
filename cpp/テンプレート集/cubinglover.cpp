#include <bits/stdc++.h>
using namespace std;
#define repl(i, l, r) for (int i = (l); i < (int)(r); ++i)
#define rep(i, n) repl(i, 0, n)
#define CST(x) cout << fixed << setprecision(x)
#define all(x) (x).begin(), (x).end()
#define sz(x) (int)(x).size()
using ll = long long;
constexpr ll MOD = 1000000007;
constexpr int inf = 1e9 + 10;
constexpr ll INF = (ll)4e18 + 10;
constexpr int dx[9] = {1, 0, -1, 0, 1, -1, -1, 1, 0};
constexpr int dy[9] = {0, 1, 0, -1, 1, 1, -1, -1, 0};
template <typename T>
using MaxHeap = priority_queue<T>;
template <typename T>
using MinHeap = priority_queue<T, vector<T>, greater<T>>;
template <typename T>
inline bool chmax(T &a, T b) {
    return ((a < b) ? (a = b, true) : (false));
}
template <typename T>
inline bool chmin(T &a, T b) {
    return ((a > b) ? (a = b, true) : (false));
}
int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
 
    int a, b;
    cin >> a >> b;
    ll ans = 1;
    rep(i, a - b) ans *= 32;
 
    cout << ans << endl;
 
    return 0;
}