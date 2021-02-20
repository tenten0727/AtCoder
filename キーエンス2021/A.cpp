#include <iostream>

using namespace std;

int main(void){
    int n;
    cin >> n;

    unsigned long long a[2*10000], b[2*10000];
    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    for(int i = 0; i < n; i++){
        cin >> b[i];
    }


    return 0;

}