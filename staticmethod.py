# Python Program To Calculate Power Value Of A Number With The Help Of A Static Method

class Myclass:
    
    # Method To Calculate x To The Power Of n
    
    @staticmethod
    def mymethod(x, n):
        result = x**n
        print(' {} To The Power Of {} Is {}'.format(x, n, result))
        
# Call The Static Method

Myclass.mymethod(5, 3)
Myclass.mymethod(5, 4)
