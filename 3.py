print("{}".format(500))

format_a = "{}만원".format(5000)
print(format_a)
format_b = "월급 {} 만원 입니다.".format(1000)
print(format_b)
format_c = "{} {} {}".format(50,60,70)
print(format_c)

output_a="{:d}".format(52)
print(output_a)
output_b = "{:5d}".format(52)
print(output_b)
output_c = "{:10d}".format(52)
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print(output_c)
print(output_d)
print(output_e)

a="Hello Python"
print(a)
print(a.upper)