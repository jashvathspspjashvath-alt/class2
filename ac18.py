sub1=float(input('enter amarks of subject 1:'))
sub2=float(input('enter a marks of subject 2 :'))
sub3=float(input('enter a marks of subject 3:'))
sub4=float(input('enter  marks of subject 4:'))
sub5= float(input('enter a marks in sub 5:'))
average = (sub1 + sub2 + sub3 + sub4+ sub5) / 5
print('average marks :', average)
if average >=90:
   grade = 'A+'
elif average >= 80:
     grade ='a'
elif average >=70:
     grade= 'B'
elif average >=60:
     grade = 'C'
elif average >=50:
     grade='d'
else:
     grade ='u failed balboyeee'
print('grade:',grade)