//classic DP problem...

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        int vectorSize = amount + 1;
        vector<int> dp(amount + 1, vectorSize);
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                
                if (coins[j] <= i) {
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        int result = dp[amount];
        
        if (result > amount){
            return -1;
        } else {
            return result;
        }
    }
};