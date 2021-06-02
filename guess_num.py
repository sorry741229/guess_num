import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint( start, end)
count = 0
while True:
	count += 1 # count = count +1
	num = input('請猜數字1~100 :') #num =使用者猜的數字
	num = int(num)
	if r == num:
		print('恭喜!終於猜對了!!')
		print('這是你猜的第', count, '次')
		break
	else:
		if num > r:
			print('你猜的數字比答案"大"')
		else:
			print('你猜的數字比答案"小"')
	print('這是你猜的第', count, '次')
