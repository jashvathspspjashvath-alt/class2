med_cau=input('enter Y or n')
attendance=int(input('enter ur per cent:'))
if med_cau=='Y':
   print('u allowed to comein')
else:
    if attendance>75:
        print(' u allowed to comein')
    else:
        print('not allowed')