// UVA 623 - 500!
// Read integers until EOF. For each n, print "n!" and the value of n!.
// Implement a simple big integer (base 10) and precompute 0!..1000!.

#include <bits/stdc++.h>
using namespace std;

// big integer as decimal digits, least-significant first
using Big = vector<int>;

static void mul(Big &a, int m) {
    int carry = 0;
    for (size_t i = 0; i < a.size(); ++i) {
        long long v = 1LL * a[i] * m + carry;
        a[i] = int(v % 10);
        carry = int(v / 10);
    }
    while (carry) {
        a.push_back(carry % 10);
        carry /= 10;
    }
}

static string to_string_big(const Big &a) {
    string s;
    s.reserve(a.size());
    for (int i = int(a.size()) - 1; i >= 0; --i) s.push_back(char('0' + a[i]));
    return s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // precompute factorials up to 1000
    const int MAXN = 1000;
    vector<string> fact(MAXN + 1);
    Big cur = {1};           // 0! = 1
    fact[0] = "1";
    for (int i = 1; i <= MAXN; ++i) {
        mul(cur, i);
        fact[i] = to_string_big(cur);
    }

    int n;
    while ( (cin >> n) ) {
        cout << n << "!\n" << fact[n] << "\n";
    }
    return 0;
}
