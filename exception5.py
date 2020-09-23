# Python Program To Handle Multiple Exceptions

def avg(list):
    tot = 0
    for x in list:
        tot += x
        avg = tot/len(list)
        return tot, avg
    
# Call The avg() And Pass A List

try:
    t, a = avg([1,2,3,4,5,'a']) # Here Give Empty List And try
    print('Total = {}, Average = {}'.format(t, a))
    
except TypeError:
    print('Type Error, Please Provide Numbers.')
    
except ZeroDivisionError:
    print('ZeroDivisionError, Please Do Not Give Empty List. ')
    