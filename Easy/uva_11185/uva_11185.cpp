// UVA 11185 - Ternary
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long n;
    while ( (cin >> n) ) {
        if (n < 0) break;
        if (n == 0) { cout << "0\n"; continue; }
        string ans;
        while (n > 0) {
            ans.push_back(char('0' + (n % 3)));
            n /= 3;
        }
        reverse(ans.begin(), ans.end());
        cout << ans << '\n';
    }
    return 0;
}
