# def my_country(country = "Rwanda"):
#     print(f"Hello from {country}")

# def greet(*names):
#      for name in names:
#         print(f"Hello {name}")



# Create  function named concatenate_args that takes any number of string 
# arguments in positional arguments format and concatenates them into a single string
def concatenate_args(*args):
    concaStr = ''
    for arg in args:
        concaStr += arg
    return concaStr

# A function named concatenate_kwargs that takes any number of string arguments in keyword 
# arguments  format and concatenates them into a single string

def concatenate_kwargs(**kwargs):
    concaVal = ''
    for key,value in kwargs.items():
        concaVal += value

    return concaVal