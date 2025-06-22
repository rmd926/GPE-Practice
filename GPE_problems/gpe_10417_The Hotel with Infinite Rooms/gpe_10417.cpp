#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    ll S, D;
    while (cin >> S >> D) {
        // 計算 discriminant，來源為推導後的不等式封閉解
        double discriminant = sqrt(4.0 * S * S + 8.0 * D - 4.0 * S + 1.0);

        // 根據數學推導，總天數 = S + ceil((sqrt_expr / 2) - S - 0.5)
        ll answer = S + (ll)ceil(discriminant / 2.0 - S - 0.5);

        cout << answer << '\n';
    }

    return 0;
}
