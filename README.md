# Kreativstorm 
## Trainig hand-on program 
trainig program divide in 5 weeks were practice concepts fundamentals and practice complex problems daylry 
### Week 1
During this week star practice with conditional, error handling problems, for detect diferents types of errors and how implement in the code
proyect euler resolb diferent problems like fibonacci sequence and practice diferent matematical operations 

In this practice review 5 ejercise for practice diferent situation in conditional  
1. Write a program that prompts the user for a string and checks whether the string is a palindrome (i.e., the string reads the same forward and backward).
```   
def main():
    value = input('Give my a string')
    
    if value == value[::-1]:
        print('string is palindrome')
    else:
        print('String isnt palindrome')

```

2. Write a program that takes in a list of integers and returns the sum of all even numbers in the list.
```
def even_number(numbers):
    evencount = 0
    for i in numbers:
        if i % 2==0:
            evencount =+ i
    return evencount
    
list_of_integers = [1,2,3,4,5,66,64,2]

result = even_number(list_of_integers)

print( "result for sum of numbers: ", result )    
```


3. Write a program that prompts the user for their age and checks whether they are old enough to vote (i.e., 18 years old or older).
```
age = int(input("Put your age for verification"))

if age >= 18:
    print("You have the correct age for Vote")
else:
    print("You do not have the correct age for Vote")
```

4. Write a program that takes in a list of integers and returns the largest number in the list that is also divisible by 3.
```
int_lit=[2,3,4,5,6,77,88,776,33,55]
soted_list = sorted(int_lit, reverse=True)


for i in soted_list:
    if i % 3 == 0:
        print(i)
        break 
        
```


5. Write a program that prompts the user for a number and checks whether the number is a prime number (i.e., only divisible by 1 and itself).
```
number =int(input("Write a number bettwen 1 and 10000"))

for i in range(1, number):
    if i % 1 and i % i ==0:
        print("It's a prime number ")
    else:
        print("It isn't a prime number")
```



# Week 2
Duriong this week practice whith diferent typees of data 

## For loops

1. Create a for loop that iterates through a list of strings and prints each string in uppercase.
```
list_of_strings = [ "example1", "example2", "example3" ]

for i in list_of_strings:
    print( i.upper())
```
## While loops

5. Create a while loop that repeatedly takes user input and keeps track of the highest number entered until the user enters "done".
```
highest =[]

while True:
    num = input('Write a number')
    if num == 'done':
        break
    nums = int(num)

    highest.append(nums)
    print(max(highest))
```

## File Handling



## Automate Email Sending

# Week 3
# Week 4
