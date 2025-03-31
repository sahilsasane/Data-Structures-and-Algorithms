#include <bits/stdc++.h>

using namespace std;
#define ll long long

void solve(string s) {
    int n = s.size();
    bool flag = false;
    do {
        flag = false;
        for (int i = n - 1; i > 0; i--) {
            if (s[i] != '0' && s[i - 1] < (char)(s[i] - 1)) {
                s[i] = char(s[i] - 1);
                swap(s[i], s[i - 1]);
                flag = true;
            }
        }
    } while (flag);
    cout << s << endl;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        solve(s);
    }
    return 0;
}