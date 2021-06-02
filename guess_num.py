import random
r = random.randint( 1, 100)
while True:
	num = input('請猜數字1~100 :') #num =使用者猜的數字
	num = int(num)
	if r == num:
		print('恭喜!終於猜對了!!')
		break
	else:
		if num > r:
			print('你猜的數字比答案"大"')
		else:
			print('你猜的數字比答案"小"')

