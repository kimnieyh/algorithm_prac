for i in range(3,0,-1):
    s = input()
    if s not in ['Fizz','Buzz','FizzBuzz']:
        n = int(s)+i

if n %15 == 0 :
    print('FizzBuzz')
elif n %3 == 0:
    print('Fizz')
elif n %5 == 0:
    print('Buzz')
else:
    print(n)
