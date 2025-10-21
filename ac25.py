print('welcome to the ride selection system ')
print('choose ur ride category:')
print('1.bike')
print('2.car')
cate=input(' enter ur cho (1 for bike / 2 for  car:')
if cate == '1':
    print('\n u selection bike.')
    print("Choose your bike type:")
    print("a. Sports Bike")
    print("b. Cruiser Bike")
    bike_type=input("Enter your choice (a/b): ")
    if bike_type.lower() == 'a':
       print("You selected a *Sports Bike* Fast and stylish ride!")
    elif bike_type.lower() == 'b':
        print("You selected a *Cruiser Bike* Comfortable and great long rides!")
    else:
         print('invalid bike type selc.')
elif cate == '2':
    print('\n u selc car.')
    print('cho ur ty car.')
    print('a.bmwm3GGTR.')