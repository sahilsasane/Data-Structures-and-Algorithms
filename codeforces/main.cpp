#include <bits/stdc++.h>

using namespace std;
#define ll long long

ll solve(ll n, ll b, ll c) {
    if(c==0 && b==0) return -1;
    if(c==0) return 0;
    
}


int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll t;
    cin >> t;
    while (t--) {
        ll n, b, c;
        cin >> n >> b >> c;
        cout << solve(n, b, c) << endl;
    }
    return 0;
}