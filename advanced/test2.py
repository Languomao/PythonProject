import re

phone = "188-1948-7061 # 这是我的电话号码"

num = re.sub(r'# .*$', "", phone)
print(num)

num2 = re.sub(r'\D', "", num)
print(num2)
