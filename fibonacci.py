def fibonacci_count(n):
   
    a, b = 1, 1
    count = 0

  
    while a <= n:
        count += 1
        a, b = b, a + b

    return count

number = int(input())


result = fibonacci_count(number)
print(result)
