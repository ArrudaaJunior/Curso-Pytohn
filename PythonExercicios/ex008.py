medida = float(input('Digite a distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dm = medida * 0.1
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a \n{:.3f}km \n{:.2f}hm \n{:.1f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dm, cm, mm))
