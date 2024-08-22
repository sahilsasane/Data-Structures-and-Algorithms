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
    string s;
    cin >> s;

    // Reading the second line (three integers)
    int a, b, c;
    cin >> a >> b >> c;

    // Reading the third line (three integers)
    int x, y, z;
    cin >> x >> y >> z;

    // Reading the fourth line (single integer)
    int k;
    cin >> k;

    // Output the values to verify they are read correctly
    cout << "String: " << s << endl;
    cout << "First set of integers: " << a << " " << b << " " << c << endl;
    cout << "Second set of integers: " << x << " " << y << " " << z << endl;
    cout << "Single integer: " << k << endl;

    return 0;
}