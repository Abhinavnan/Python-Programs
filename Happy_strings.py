'''
The k-th Lexicographical String of All Happy Strings of Length n
A happy string is a string that:
consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:
Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.

Example 3:
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 
["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

Constraints:
1 <= n <= 10
1 <= k <= 100
'''
def getHappyString(n: int, k: int) -> str:
        power = int(pow(2, n - 1))
        c = 3 * power
        if k > c or n < 1:
            return ""
        else:
            s = ['a', 'b', 'c']
            position =int(k/power)
            if k % power == 0:
                position -= 1
            if position == -1:
                position = 2
            n -= 1
            spliter = int(power/2)
            if position == 0:
                k = pow(2, n -1) + k
            elif position == 1:
                k = k - power
                if k > spliter:
                    k = k + pow(2, n -1)
            else:
                k = k - power * 2     
            return s[position] + getHappyString(n, k)
n = int(input("Enter the length of the string: "))
k = int(input("Enter position: "))
print("Happpy string is:",getHappyString(n, k))



        