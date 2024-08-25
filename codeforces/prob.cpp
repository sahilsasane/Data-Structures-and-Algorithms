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
    
    ll n;
    cin >> n;
    vector <ll> vec;
    ll max_index = 0, min_index = 0;
    for(ll i = 0; i< n; i++){
        ll k;
        cin >> k;
        vec.push_back(k);
        if(k > vec[max_index]) max_index =  i;
        if(k <= vec[min_index]) min_index = i;
    }
     if (n == 2) {
        if (vec[0] >= vec[1]) {
            cout << 0;
        } else {
            cout << 1;
        }
    } else {
        if (min_index < max_index) {
            cout << max_index + n - (min_index + 2);
        } else {
            cout << max_index + n - min_index - 1;
        }
    } 

    return 0;
}