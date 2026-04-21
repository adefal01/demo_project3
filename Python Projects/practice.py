def not_string(s):
    if s.startswith("not"):
        return s
    return "not" + s


print(not_string("cat"))
print(not_string("not"))
print(not_string("apple"))
def swap(lst):
    min_index=lst.index(min(lst))
    lst[0],lst[min_index]=lst[min_index],lst[0]
    return lst
"""
Given a list, find the minimum element in the list and swap it with the first
element in the list. Return the list.
swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
"""
print(swap([5,4,3,2,1]))
print(swap([3,1,4,2]))

def count_spaces(string):
    return len([c for c in string if c==" "])

print(count_spaces("the cow jumped over the moon"))
"""
Use comprehension to count the number of spaces in a string.
*** Important: your code must use comprehensions and should not be more than
two lines of code including the return statement ***
count_spaces("the cow jumped over the moon") returns 5
"""
def sum67(nums):
    total=0
    skip=False

    for n in nums:
        if n==6:
            skip=True
        elif n==7 and skip:
            skip=False
        elif not skip:
            total+=n
    return total
'''
Return the sum of the numbers in the array, except ignore sections
of numbers starting with a 6 and extending to the next 7
(every 6 will be followed by at least one 7).
Return 0 for no numbers.
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
'''
print(sum67([1,2,2]))
print(sum67([1,2,2,6,99,99,7]))
print(sum67([]))

def minmaxdiff(nums):
    return max(nums)-min(nums)


print (minmaxdiff([1,2,3,4,5]))
print (minmaxdiff([10]))
print (minmaxdiff([-3,7,2]))
