# 1(i)
def area_of_a_circle():
    radius = int(input("Enter the radius of the circle: "))
    pie = 3.14
    area = pie*radius**2
    print(f'The area of the circle with radius{radius} is {area:.3f}')
area_of_a_circle()




# 1(ii)
numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0
for num in numbers:
    if num % 2 != 0:
        odd_sum += num
print("Sum of odd numbers:", odd_sum)



# 1(iii)
def calculate(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    return sum, difference, product, quotient
num1 = 10
num2 = 5
result = calculate(num1, num2)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Quotient:", result[3]) 



# 1(iv)
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student_info['age'] = 26
student_info['city'] = 'Kampala'
print(student_info)
