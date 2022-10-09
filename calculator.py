점수 = eval(input('>> 점수를 입력하시오. '))

if 점수 >= 90:
    print("A 입니다.")
elif 90 > 점수 >= 80:
    print("B 입니다.")
elif 80 > 점수 >= 70:
    print("C 입니다.")
elif 70 > 점수 >= 60:
    print("D 입니다.")
else:
    print("F 입니다.")
    
