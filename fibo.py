a = 0
b = 1
num1 = int(input("Enter number of iteration:"))

while(num1 >= 0):
    ans = a + b
    a = b
    b = ans
    print(ans)
    num1 -= 1