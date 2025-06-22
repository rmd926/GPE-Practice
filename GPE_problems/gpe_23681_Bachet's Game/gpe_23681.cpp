#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    while (cin >> n >> m) {
        vector<int> moves(m);
        for (int i = 0; i < m; ++i) cin >> moves[i];

        vector<bool> dp(n + 1, false);

        for (int i = 1; i <= n; ++i) {
            for (int move : moves) {
                if (i - move >= 0 && !dp[i - move]) {
                    dp[i] = true;
                    break;
                }
            }
        }

        if (dp[n]) cout << "Stan wins\n";
        else cout << "Ollie wins\n";
    }
    return 0;
}
