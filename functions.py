#def function_name(parameter1, parameter2)
    #add = parameter1 + parameter2
    #return add
#function_name(argument1, argument2)

def find_sum(priceList):
    sum = 0
    for item in priceList:
        sum = sum+item
    return sum

priceList1 = [4.3, 2.7, 12.6]
priceList2 = [6.3, 11, 18.4]

sum1  = find_sum(priceList1)
sum2  = find_sum(priceList2)

print("Sum of list1:$",sum1)
print("Sum of list2:$",sum2)