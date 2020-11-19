#include <iostream>
#include <vector>
using namespace std;
const long long INF = 1LL << 60;

int main(){{
    // input
    int H, W;
    cin >> H >> W;
    vector< vector<int> > field(H, vector<int>(W, 0));

    for (int h = 0; h < H; ++h){
        // "..."はstring、一度に入力される
        string el;
        cin >> el;
        for (int w = 0; w < W; ++w){
            cout << el[w] << endl;
            char cell = el[w];
            // "..."の文字列から１文字ずつ取り出して"#"と一致するかcheckしたいだけなのに...
            // すごい詰まった。
            // pointer adn intの比較？なんてしたつもりないぞ
            // comparison between pointer and integer ('char' and 'const char *')
            // 
            // 
            // 数値のように「==」を用いて比較するとアドレスが同じか否かの比較になる。
            // field[h][w]
            char target = ".";
            cout << strcmp(el[w], target) << endl;
        }}


    cout << field[H-1][W-1] << endl;
    vector<vector<int> > dp(H, vector<int>(W, -1));

    // initialization
    dp[0][0] = 1;

    // for (int i=1; i < N; ++i){
    //     if (i == 1) dp[i] = abs(h[i] - h[i-1]);
    //     else dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), 
    //         dp[i-2] + abs(h[i] - h[i-2]));
    // }
    // cout << dp[N-1] << endl;

}}