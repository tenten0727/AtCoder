#include <iostream>

using namespace std;

int main(void){
    long long N;
    long long D;
    long long count = 0;

    cin >> N >> D;

    for(int i = 0; i < N; i++){
        long long x, y;
        cin >> x >> y;
        long long dis = x*x + y*y;
        if(dis <= D*D){
            count++;
        }
    }

    cout << count << endl;

    return 0;
}