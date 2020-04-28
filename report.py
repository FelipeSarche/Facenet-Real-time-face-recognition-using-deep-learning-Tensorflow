import csv
import os

directorioImagenesReconocidas ='../Clasificada/Reconocidas'
directorioReporte = '../Reporte'

try:
  os.stat(directorioReporte)
except:
  os.mkdir(directorioReporte)

listadirectorios = os.listdir(directorioImagenesReconocidas)
listadirectorios.sort()

f = open(directorioReporte+'/csvfile.csv','w')

for fechacarpeta in listadirectorios:
	f.write(str(fechacarpeta)+'\n') 
	listaimagenes = os.listdir(directorioImagenesReconocidas+"/"+str(fechacarpeta))
	listaimagenes.sort()
	for foto in listaimagenes:
		#f.write(foto.strip('.png')[20::] +'\r') 
		f.write(foto.strip('.png')[20::] + ',' + foto.strip('.png')[10:20] +'\n') 




#nms = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

#f = open('numbers2.csv', 'wb')

#with f:

 #   writer = csv.writer(f)
    
  #  for row in listadirectorios:
   #     writer.writerow(nms)
