try:
    num1=float(input("enter first number :"))
    num2=float(input("enter secound number :"))

    print("..............................")
    print("on dividing ",num1,"by",num2)
    print("quotient:",(num1/num2))
    print(".................................." )
except ValueError:
    print("unexpected data type ") 
except ZeroDivisionError:
    print("unable to divide by 0")
else:
    print("...........................")
finally  :
    print("...program executed .....")     