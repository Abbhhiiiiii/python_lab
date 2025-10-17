def rev(num):
    rev_num = 0
    while num > 0:
        temp = num % 10
        rev_num = rev_num * 10 + temp
        num = num // 10
    return rev_num

def num():
    n = int(input("Enter a Number (minimum 4 digits): "))  

    if n > 1000:
        re = rev(n) 
        print("Original number:", n)
        print("Reversed number:", re)
    else:
        print("Enter a Number Greater than 1000")

num()
