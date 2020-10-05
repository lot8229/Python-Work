import datetime

now = datetime.datetime.now()

# if now.hour < 12 : 
#     print("현재시간은 {}로 오전입니다.".format(now.hour))
# if now.hour >=12 : 
#     print("현재시간은 {}로 오후입니다.".format(now.hour))
if 3>=now.month:
    print("이번달은 {}월로 봄입니다.".format(now.month))
if 6>=now.month:
    print("이번달은 {}월로 여름입니다.".format(now.month))
if 9>=now.month:
    print("이번달은 {}월로 가을입니다.".format(now.month))
if 12==now.month or 1<=now.month:
    print("이번달은 {}월로 겨울입니다.".format(now.month))


