# Python program to calculate positive number square root
import cmath
num = 856

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f' % (num, num_sqrt))


# Find the square root of a real or complex number
# import complex math module

num = 4+44j

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num,
      num_sqrt.real, num_sqrt.imag))
