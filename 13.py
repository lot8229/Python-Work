number=[273,103,5,32,65,9,72,800,99]
#실행결과 :
# 273은 3자릿수입니다
# 103은 3자릿수입니다
# 5는 1자릿수입니다

for i in number:
    print(i,"는",len(str(i)),"자릿수입니다.")