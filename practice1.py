
def hello_name(user_name):
    return ("hello_" + user_name.upper() + "!")
 
print(hello_name("Tyler Cook"))





def first_odds(n):
    numbers = list(range(0, 101))
    for number in numbers:
        if number % 2 !=0:
            print(100)



def max_num_in_list(a_list):
        if x > max : 
            return max

a_list= [1, 2, 3, 4, 5]
print(max(a_list))




def is_leap_year(a_year):
    leap = False

    if (a_year % 4 == 0) and (a_year % 100 != 0):
        leap = True
    elif (a_year % 100 == 0) and (a_year % 400 != 0):
        leap = False
    elif (a_year % 400 == 0):
        leap = True 
    else:
        leap = False 
    return leap

print(is_leap_year(2000))




def is_consecutive(a_list):
    i = 0 
    status = True
    while i < len(a_list)-1:
        if a_list[i]+1==a_list[i+1]:
            i =+ 1
        else:
            status = False
            break
        print(status)