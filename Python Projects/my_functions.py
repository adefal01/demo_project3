"""
for this function Im taking a list and 
returning the sum of all values in the list
"""
def sum_list(numbers):
    total=0
    for num in numbers:
        total+=num
    print("Sum:",total) 

#3 trial runs
trial_1=[1,2,3,4]
sum_list(trial_1)
trial_2=[2,4,6,8,10]
sum_list(trial_2)
trial_3=[1,3,5,7]
sum_list(trial_3)

"""
for this function I am using strings to state the name of a person and
where they are from
"""
def greeting(name,location):
    print("Hello my name is",name, ", I am from", location)

#3 trial runs
greeting("Ava", "Pennslyvania")
greeting("Brooke", "New York")
greeting("Sophia", "New Jersey")
