#include <iostream>
#include <math.h>
#include <ctime>

using namespace std;
bool is_prime_number(long long n){
    bool is_pn = true;
    for (int i = 2; i < round(sqrt(n))+1; i++){
        if (n % i == 0){
            is_pn =false;
            break;
        }
    }
    return is_pn;
}


long long find_prime_number(long long n){
    while (n % 6 != 0)
        n++;
    while (true){
        if (is_prime_number(n+1))
            return n+1;
        else if (is_prime_number(n+5))
            return n+5;
        n+=6;
    }
}


int main() {
    long long s = 21000000;
    long long n = find_prime_number(s);
    cout << " " << clock() / 100000000.0 << "\n";
    cout << n;
    return 0; 
}