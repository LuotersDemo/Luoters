'''
66. 加一


'''

class Solution:
    def plusOne(digits):
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i+1, n):
                    digits[j] = 0

                return digits

        return [1] + [0]*n

    if __name__ == '__main__':
        # digits = [4, 3, 2, 1]
        digits = [1, 3, 5, 7, 9, 9]
        # digits = [9, 9, 9]

        print(plusOne(digits))


