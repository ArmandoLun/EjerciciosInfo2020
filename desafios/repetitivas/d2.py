# Desafio 2 - Recoleccion de cigarrillos

menor100=0
mayor100=0
mayor200=0

print("Ingrese cantidad de personas")
personas=int(input())

for i in range(personas):
    print("Cuantas colillas recogió?")
    cantRec=int(input())
    if(cantRec>=200):
        mayor200+=1
    elif(cantRec>=100 and cantRec<200):
        mayor100+=1
    elif(cantRec<100):
        menor100+=1


print('%.1f'%(mayor200*100/personas),"% de personas recogieron mas de 200 colillas")
print('%.1f'%(mayor100*100/personas),"% de personas recogieron mas de 100 colillas")
print('%.1f'%(menor100*100/personas),"% de personas recogieron menos de 100 colillas")