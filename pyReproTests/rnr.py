# def minimumFlips(target):
#     initial = "0" * len(target)
#     flips = 0
#
#     for i in range(len(target)):
#         if target[i] != initial[i]:
#             initial = initial[:i] + str(1 - int(initial[i])) + initial[i + 1:]
#             flips += 1
#
#     return flips

def minFlips(target):
    curr = '1'
    count = 0

    for i in range(len(target)):

        # If curr occurs in the final string
        if (target[i] == curr):
            count += 1

            # Switch curr to '0' if '1'
            # or vice-versa
            curr = chr(48 + (ord(curr) + 1) % 2)

    return count

def minimumFlips(target):
    n = len(target)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        if target[i] != target[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    return dp[-1]
def minimumFlipss(target):
    initial_str = '0' * len(target) # Initialize initial string with zeros
    flips = 0
    for i in range(len(target)):
        if initial_str[i] != target[i]:
            initial_str = initial_str[:i] + target[i] + initial_str[i+1:]
            flips += 1

    return flips

print(minFlips("01011"))
