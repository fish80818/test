import random

r = random.randint(1, 100)
while True:
	num = input('請猜數字: ')
	num = int(num) # 字串轉換成整數
	if num == r:
		print('你猜中了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小') 
