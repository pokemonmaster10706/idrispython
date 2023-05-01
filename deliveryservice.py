import colorama  #install colorama module for Python
from colorama import Fore

print(Fore.WHITE + 'Welcome to python delivery service!! \nPlease input the dimentions and weight of your parcel in centimetres and kilograms respectively.')
print('\nEach dimetion must not be more than 80 cm, \nThe sum of all dimentions must not be more than 200 cm, \nparcel must be less than 10 kilograms and more than 1 kilogram')
n = int(input('\nPlease enter how many parcels you wish to order : '))
accepted = []
rejected = []
result = False
p_sum = 0
for i in range(1, n+1):
    l=True
    b=True
    h=True
    w=True
    s=True
    length = int(input(Fore.WHITE + '\nPlease enter the length of your parcel in centimeters : '))
    if length > 80 or length < 1:
        print(Fore.RED + 'dimention out of range')
        l=False
    breadth = int(input(Fore.WHITE + 'Please enter the breadth of your parcel in centimeters : '))
    if breadth > 80 or breadth < 1:
        print(Fore.RED + 'dimention out of range')
        b=False
    height = int(input(Fore.WHITE + 'Please enter the height of your parcel in centimeters : '))
    if height > 80 or height < 1:
        print(Fore.RED + 'dimention out of range')
        h=False
    if length+breadth+height > 200:
        print(Fore.RED + '\nthe sum of all the dimentions can not be more than 200 cm, ')
        s=False
    weight = int(input(Fore.WHITE + 'Please enter the weight of your parcel in kilograms : '))
    if weight > 10 or weight < 1:
        print(Fore.RED + 'weight out of range')
        w=False
    if l is False or b is False or h is False or w is False or s is False:
        print(Fore.RED + '\nSorry, this parcel has been rejected for the following reasons :')
    else:
        print(Fore.GREEN + '\nparcel accepted!!')

        result = True
    if l is False:
        print(Fore.RED + 'length is greater than 80 cm,')
    if b is False:
        print(Fore.RED + 'breadth is greater than 80 cm,')
    if h is False:
        print(Fore.RED + 'height is greater than 80 cm,')
    if w is False:
        print(Fore.RED + 'weight is greater than 10 kg,')
    if s is False:
        print(Fore.RED + 'sum of dimentions is greater than 200 cm,')
    if weight <= 5:
        price = 10
    elif weight > 5:
        price = 10 + (((weight-5)*1000)/100)*0.1
    d_parcel = {'length':length,'breadth':breadth,'height':height,'weight':weight,'price':price}
    if l is False or b is False or h is False or w is False or s is False:
        rejected.append(d_parcel)
    else :
        accepted.append(d_parcel)
        p_sum += price
    print(Fore.BLUE + '\nparcel',i,'complete')

print(Fore.RED + '\nthe number of rejected parcels is:', len(rejected))
for i in range(len(rejected)) :
    print(Fore.RED + '\nparcel ',i+1,'-- ',' length ',rejected[i]['length'],'cm,',' breadth ', rejected[i]['breadth'],'cm,',' height ', rejected[i]['height'],'cm,',' weight ', rejected[i]['weight'],'kg,',sep='')
print(Fore.GREEN + '\nthe number of accepted parcels is:', len(accepted))
for i in range(len(accepted)) :
    print(Fore.GREEN + '\nparcel ',i+1,'-- ',' length ',accepted[i]['length'],'cm,',' breadth ', accepted[i]['breadth'],'cm,',' height ', accepted[i]['height'],'cm,',' weight ', accepted[i]['weight'],'kg,',' price ', accepted[i]['price'],'$')

if result is True:
    print(Fore.CYAN + '\n\nThe total price of all your parcels is :','$',p_sum)
    print('your parcels will be delivered within 3 business days.')
    print('Thankyou for using Python delivery services\nwe hope to see you soon!!')
    print(Fore.WHITE + '')
else:
    print('sorry, none of your parcels were accepted since they were all out of range in one way or another\nThankyou for using python delivery\nwe are sorry for the trouble.')
    print(Fore.WHITE + '')
