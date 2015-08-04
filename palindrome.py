__author__ = 'KH1962'
def even_case(number):
    number=str(number)
    le=len(str(number))
    mn=le/2
    num1=str(number)[:le/2]
    #num2=str(number)[len(str(number))/2:]
    if [str(number)[str(number)[mn-1]<str(number)[mn]]]:
        str(number)[mn-1]=str(number)[mn-1]+1
        num2=num1[::-1]
    if [str(number)[str(number)[mn-1]>str(number)[mn]]]:
        num2=num1[::-1]

    number=num1+num2

    print num1,num2,number
    print le,mn
    print str(number)[mn-1],str(number)[mn]

even_case(1234)

#a=123
#print str(a)[len(str(a))/2:]
#b=123445
#print str(b)[len(str(b))/2]
#print str(b)[len(str(b))/2:]