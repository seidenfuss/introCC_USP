segundos=int(input("Insira o numero de segundos que quer converter: "))

dias=segundos//(3600*24)
horas_restantes=segundos%(3600*24)

horas_final=horas_restantes//3600
segs_restantes=segundos%3600

minutos=segs_restantes//60
segs_final=segs_restantes%60

print(dias,"dias,", horas_final,"horas,", minutos,"minutos e", segs_final,"segundos.")
