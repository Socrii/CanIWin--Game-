print('Welcome to the Game World ')
print('Here are the following instruction to play : ')
print(' two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.')
print('What if we change the game so that players cannot re-use integers? For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.')
print('Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.')

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Example 1:')
print('Input: maxChoosableInteger = 10, desiredTotal = 11')
print('Output: false')
print('Explanation:')
print('No matter which integer the first player choose, the first player will lose.The first player can choose an integer from 1 up to 10.')
print('If the first player choose 1, the second player can only choose integers from 2 up to 10.')
print('The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.')
print('Same with other integers chosen by the first player, the second player will always win.')

print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Example 2:')
print('Input: maxChoosableInteger = 10, desiredTotal = 0')
print('Output: true')
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Example 3:')
print('Input: maxChoosableInteger = 10, desiredTotal = 1')
print('Output: true')
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

def solve(remaining, mask, maxChoosableInteger, dp):
    if remaining <= 0:
        return False
    if mask in dp:
        return dp[mask]
    for i in range(1, maxChoosableInteger + 1):
        if (mask & (1 << (i - 1))) == 0:
            if not solve(remaining - i, mask | (1 << (i - 1)), maxChoosableInteger, dp):
                dp[mask] = True
                return True
    dp[mask] = False
    return False
def canIwin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= 0:
        return True
    totalSum = maxChoosableInteger * (maxChoosableInteger + 1) / 2
    if totalSum < desiredTotal:
        return False
    dp = {}
    return solve(desiredTotal, 0, maxChoosableInteger, dp)

desiredTotal = int(input('Enter the Target to reach first: '))
maxChoosableInteger = int(input('Enter the maximum choosable number from 1 till maxchoosable number: '))
print('Desired total is', desiredTotal, 'and max choosable number is', maxChoosableInteger)
print('Let\'s play')
if canIwin(maxChoosableInteger, desiredTotal):
    print("True")
else:
    print("False")  
