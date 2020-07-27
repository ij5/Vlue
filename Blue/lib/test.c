#include <math.h>

#define true (1)
#define false (0)


int isprime(int n){
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    if (n < 9) return false;
    int k = 5;
    int l = (int)(sqrt((double)n) + 0.5);
    while (k <= l) {
        if (n % k == 0 || n % (k + 2) == 0) return false;
        k += 6;
    }
    return true;
}