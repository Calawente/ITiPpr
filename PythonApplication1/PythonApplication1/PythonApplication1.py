HEIGHT = 175
WEIGHT = 90
steps = int(input("Количество шагов: "))
time = int(input("Время: "))
def CalCalc(h,w,s,t):
	return 0.035 * w + ((s/t)**2 / h) * 0.029 * w

print(f"Калорий сожжено: {CalCalc(HEIGHT,WEIGHT,steps,time)}; Пройденная дистанция: {steps/time}")