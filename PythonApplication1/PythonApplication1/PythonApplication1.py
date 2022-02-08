HEIGHT = 175
WEIGHT = 90
steps = int(input("Количество шагов: "))
time = int(input("Время: "))
def cal_calc(h,w,s,t):
	return 0.035 * w + ((s/t)**2 / h) * 0.029 * w

print(f"Калорий сожжено: {cal_calc(HEIGHT,WEIGHT,steps,time)}; Пройденная дистанция: {steps/time}")
l_step = HEIGHT / 4 + 0.37
dist = steps * l_step / 100000
print(f"Дистанция в км: {dist}")
if dist < 2:
	print("Пожнажми!")
elif dist < 4:
	print("Хорошо!")
else:
	print("Отлично!")

word = input("Введите слово: ")
def is_palindrome(w):
	for i in xrange(0, len(w)/2):
		if w[i] != w[len(w)-i-1]:
			return False
	return True
if is_palindrome(word) == True:
	print("Слово - палиндром")
else:
	print("Слово - не палиндром")
