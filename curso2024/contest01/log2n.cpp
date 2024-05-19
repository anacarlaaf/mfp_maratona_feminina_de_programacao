#include <iostream>
using namespace std;

int main() {
    long long n;
    cin >> n;
    int k = 0;
    while ((1LL << k) <= n) {
        k++;
    }
    cout << k - 1 << "\n";
    return 0;
}