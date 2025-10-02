weigth=float(input('enter ur weigth kg:'))
heigth= float (input('enter urr heigth m'))
bmi= weigth /(weigth*heigth*2)
print('ur bmi is :',bmi)
if bmi< 18.9:
    print('u are underkg')
elif bmi>=18.5 and bmi<24.9:
    print('u have normal kg')
elif bmi>=25 and bmi<29.9:
    print('u are over kg')
else:
    print(' u are fatty')