#include <iostream>
#include <vector>

using namespace std;

int main(void){
    long long K;
    long long ans;
    cin >> K;

    if(K % 2 == 0){
        ans = -1;
    }
    else{
        unsigned long long num = 7;
        for(long long i = 1; ; i++){
            if(num % K == 0){
                ans = i;
                break;
            }
            num = num*10 + 7;
        }
    }

    cout << ans << endl;

    return 0;

}