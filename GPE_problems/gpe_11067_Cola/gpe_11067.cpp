#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    while ( (cin >> N) ) {
        long long n = N;
        long long ans = n;

        // 不斷用空瓶換新可樂
        while (n >= 3) {
            long long exch = n / 3;        // 本輪能換多少瓶
            ans += exch;                   // 累計喝到的可樂
            n = exch + (n % 3);            // 換完後剩下的空瓶加上本輪換不掉的空瓶
        }

        // 如果最後剩 2 個空瓶，可以「借」1 瓶，喝完後用空瓶還掉
        if (n == 2) {
            ans += 1;
        }

        cout << ans << "\n";
    }

    return 0;
}
