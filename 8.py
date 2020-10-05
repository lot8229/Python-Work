num = input("정수입력>>")
last_num = num[-1]

if last_num in "02468":
    print("짝수입니다.")
if last_num in "13579":
    print("홀수입니다.")