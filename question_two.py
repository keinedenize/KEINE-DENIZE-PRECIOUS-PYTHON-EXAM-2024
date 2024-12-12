# 2(i)
# Student details
def student_details():
    student_name = input ("Enter the student name : ")
    student_number = input("Enter the students number : ")
    programming = int(input("Enter marks scored in programming : "))
    Data_Science = int(input("Enter the marks scored in Data science : "))
    computer_applications = int(input("Enter the marks scored in computer appliactions : "))
    sum = programming + Data_Science + computer_applications
    Average = (sum)/3
    print(f"The Average mark {student_name} with the following marks in programming {programming} , Data science {Data_Science} and computer applications {computer_applications} is {Average:.3f}")
student_details() 



# 2(ii)
def miles_per_gallon_used():
     milesDriven = int(input("Enter miles driven :"))
     gallonsOfGasUsed = int(input("Enter the number of gallons used :"))
     MPG = milesDriven / gallonsOfGasUsed
     print(f"The car's miles per gallon used is {MPG:.3F}") 
miles_per_gallon_used() 



# 2(iii)
def odd_numbers():
    for numbers in range(1,100,2):
        print(numbers)
odd_numbers() 
