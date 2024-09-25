#include <bits/stdc++.h>

using namespace std;
#define ll long long

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    ll t;
    cin >> t;
    for(ll test_case = 0; test_case < t; test_case++){
        ll n, h;
        vector <ll> time;
        cin >> n >> h;
        for(ll i = 0; i < n; i++) {
            ll j;
            cin >> j;
            time.push_back(j);
        }
        ll i = 0, j = 1e18;
        ll k = j;
        while( i <= j) {
            ll mid = (i + j) / 2;
            ll damage = 0;
            for(ll z = 0; z < n - 1; z++) {
                if(time[z] + mid >= time[z + 1])
                    damage += time[z + 1] - time[z];
                else 
                    damage += mid;
            }
            damage += mid;
            if(damage >= h){
                k = min(k,mid);
                j = mid  - 1;
            } else {
                i = mid + 1;
            }
        }
        cout << k << endl;
    }
    return 0;
}