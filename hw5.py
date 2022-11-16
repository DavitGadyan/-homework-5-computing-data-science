import csv
import datetime

import pandas as pd
from geopy import distance
# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#
def car_at_light(light: str) -> str:
    '''Define action to take under light

    Args:
        light str: traffic light color
    Returns:
        str
    '''
    if light == 'red':
        return 'stop'
    elif light == 'green':
        return 'go'
    elif light == 'yellow':
        return 'wait'
    else:
        raise Exception (f"Undefined instruction for color: {light}" )

# print(car_at_light(light='yellow')) 

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

def safe_subtract(first_val, second_val):
    '''Substract the second value from the first value

    Args:
        first_val: first value
        second_val: second value
    '''
    try:
        return first_val - second_val
    except TypeError:
        return None
    except Exception as e:
        return e

# print(safe_subtract(first_val=set([1,1,2]), second_val=set([3])))

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl
p1 = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
p2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}


def retrieve_age_eafp(person: dict):
    '''Return age of person per EAFP

    Args:
        person dict
    '''
    try:
        return person['birth']
    except KeyError:
        print('birth key is missing from person dictionary!!')

# print(retrieve_age_eafp(person=p1))

def retrieve_age_lbyl(person: dict):
    '''Return age of person per LBYL

    Args:
        person dict
    '''
    if 'birth' in person.keys():
        return person['birth']
    else:
        print('birth key is missing from person dictionary!!')

# print(retrieve_age_lbyl(person=p1))

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#
def read_data():
    '''Read dataframe  
    '''
    try:
        with open("data.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
    except FileNotFoundError:
        print('data.csv does not exist!!!')

# print(read_data())

# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double

## beforehand we were adding up elem and not double value
### total_double_sum += elem

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings += string + " "

strings = strings.strip()

## beforehand we were adding same string 2 times. and based on popular movie groot
# was saying each word one time so removed last string and need to add up not just 
# rewrite full strings. also replace '_' with blank space ' ' and strip at the end.
## strings = string+"_"+string

### (c) Careful!
j=10
while j > 0 and j < 100:
   j += 1

### while loop that never stops. need a condition to break like of it reaches 100
## and then breaks

### (d)
productory = 1
for elem in [1, 5, 25]:
    productory *= elem
### initial value for productory was 0 which made it no matter how many terms you multiply by
### it returns 0. Productory is bascially product of all number and to make this logical 
### initial value for productory should be 1 for the code to work.


################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
l_strings = ["Simba and Nala are lions.", "I laugh in the face of danger.",
 "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
def count_simba(l_strings: list) -> int:
    '''Count simba in list of string

    Args:
        l_strings list: list of strings
    '''

    # if you mean how many time Simba appears in list of string in total
    return sum(list(map(lambda x: x.count('Simba'), l_strings)))

    # if you mean how many time Simba appears in list of string in each string
    # return list(map(lambda x: x.count('Simba'), l_strings))

# print(count_simba(l_strings))

# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

def get_day_month_year(l_datetimes: list) -> pd.DataFrame:
    ''' Create padnas dataframe of year, month and day

    Args:
        l_datetimes list: list of datetimes.date

    Returns:
        datetime_df pd.DataFrame: dataframe woth year, month and day
    '''
    m_o = map(lambda x: pd.DataFrame({'day': [x.day], 'month': [x.month], 'year': [x.year]}), l_datetimes)
    datetime_df = pd.concat(list(m_o)).reset_index(drop=True)

    return datetime_df

# print(get_day_month_year(l_datetimes=[datetime.date.today(), datetime.date.today() - datetime.timedelta(days=1)]))

# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

l_t_long_lat = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]

def compute_distance(l_t_long_lat: list):
    '''Calculated distance

    Args:
        l_t_long_lat list

    '''
    return list(map(lambda x: distance.distance(x[0], x[1]).km, l_t_long_lat))

# print(compute_distance(l_t_long_lat))

#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#


list_1 = [[2], 3, [[1,2],5]]
list_2 = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]

def sum_general_int_list(int_l):
    '''Sum all

    Args:
        int_l list: list of of integers or lists of integers
    
    '''
    total_sum = 0
     
    for j in range(len(int_l)):
       
        if isinstance((int_l[j]), list):         
            # if list call the same function if
            total_sum+= sum_general_int_list(int_l[j])
        else:
            # if it's a number
            total_sum += int_l[j]  
             
    return total_sum

# print(sum_general_int_list(int_l=list_1))