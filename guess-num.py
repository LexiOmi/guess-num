# 產生一個隨機整數1~100(不要印)
# 讓使用者重複輸入數字去猜
# 才對 => 印出 "終於猜對了!"
# 猜錯要告訴他比答案大/小

import random

r = random.randint(1, 100)
while True:
	number = input('猜數字(1~100):')
	number = int(number)
	if number == r:
		print('終於猜對了!')
		break
	elif number < r:
		print('比答案小!')
	elif number > r:
		print('比答案大!')
	

