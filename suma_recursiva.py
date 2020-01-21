# -*- coding: utf-8 -*-
def suma_descendente(number):
    if number==0:
        return 0
    else:
        return number+suma_descendente(number-1)

def sumar_recursivo(numbers):

    if len(numbers)==0:
        return 0
    elif len(numbers)==1:
        return numbers[0]
    else:
        return numbers[0]+sumar_recursivo(numbers[1:])


def run():
    print("Enter 1 or more numbers when you like and finish with 0")
    numbers=[]
    num=1
    while(num!=0):
        num=int(raw_input("Enter a number(s): "))
        numbers.append(num)

    if numbers[0]==0:
        print("Your sum is : 0")
    elif len(numbers)==2:
        print("In this case because is a 1 number is a descending sum")
        print("The result of sum is: {}".format(suma_descendente(numbers[0])))
    else:
        print("In this case sum the all numbers you entry")
        print("The result of sum is: "+str(sumar_recursivo(numbers[:-1])))



if __name__ == "__main__":
    print("*-------------------------------------------------------*")
    print("| W E L C O M E  T O  R E C U R S I V E   A D I T I O N |")
    print("*-------------------------------------------------------*")
    run()
#----------------------------
