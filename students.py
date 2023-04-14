# def year_birth(name,age):
#     year = 2023 - age
#     print(f"Hello {name} you were born in {year}")

# def sum(*numbers):
#     answer = 0
#     for number in numbers:
#         answer += number


#     return answer

    #Create a function that accept any number of integers and 
    # return the result of multiply all of them in python 

# def multiply(*nums):
#     answer = 1
#     for num in nums:
#         answer *= num
#     return answer

def student_attributes(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} :{value}")