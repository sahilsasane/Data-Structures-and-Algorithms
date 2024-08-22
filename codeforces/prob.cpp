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
    
    ll x1,x2,x3;
    cin>>x1>>x2>>x3;
    ll i = min({x1,x2,x3}), j = max({x1,x2,x3});
    ll dist = LLONG_MAX;
    ll pos;

    while(i<=j){
        ll mid = (i + j) / 2;
        ll temp = abs(x1-mid) + abs(x2-mid) + abs(x3-mid);
        if(dist > temp){
            dist = temp;
            i = mid+1;
            pos = mid;
        }else{
            j = mid-1;
        }
        if (mid == i || mid == j) break;
    }
    cout<<dist;
    return 0;
}