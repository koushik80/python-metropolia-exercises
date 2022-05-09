#E-4.3:For in range
#Problem: In this program, build a calculator, which asks the user for a number,
# and calculates the sum of all positive numbers from 0 to the usergiven input.
# If the user gives the number 4, the program calculates the sum 0+1+2+3, if 7, the calculation is 0+1+2+3+4+5+6.
# Finally, the program produces an answer with the printout "The sum was:" and an answer.


#When working correctly, the program prints something like this:

          # >>>Give a number: 3
          # The sum was: 3
          # >>>

          # Give a number: 5
          # The sum was: 10
          # >>>

#Solution:

number = int(input("Give a number: "))
result = int(0)

for x in range(0, number):
    result += x

print("The sum was: ", result)
