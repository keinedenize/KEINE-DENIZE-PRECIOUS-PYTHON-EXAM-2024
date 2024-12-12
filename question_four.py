# 4(i)
# Object-Oriented Programming is a programming model based on the concept of objects.
# Its significance, makes code more organised and readable  


# B)
# A class is a blue print for creating objects while object is an instance of class


# 4(ii)
sentences = "python exam"
words = sentences.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
      word_count[word] = 1
print(word_count)



# # 4(iii)
def sum_of_numbers():
   a = int(input("Enter the first number : "))
   b = int(input('Enter the second number :'))
   sum = a + b
   print(f"The sum of the numbers {a} and {b} is {sum}")
sum_of_numbers()




# 4(iv)
class Car:
    def __init__(self,brand , name, color):
       self.brand=brand
       self.name=name
       self.color=color
 
b2=Car("mercedes-Benz" , "G-wagon", "Black") 
print(b2.brand)
print(b2.name)
print(b2.color)




# 4(v)
class car:
    def __init__(self,start_engine):
       self.start_engine=start_engine
data = car("The engine of the car has started.")      
print(data.start_engine)








