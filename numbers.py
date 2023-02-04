print('enter four numbers')
first_number = float(input('input first number: '))
second_number = float(input('input second number: '))
third_number = float(input('input third number: '))
fourth_number = float(input('input fourth number: '))

sum1 = first_number + second_number
sum2 = third_number + fourth_number
division_sums = sum1 / sum2

print("the result of dividing the sum of the first two numbers by the sum of the second two numbers: %.2f" % (division_sums))
