    import numpy as np
    from numpy import linalg as LA
    from scipy import signal
    import matplotlib.pyplot as plt


# Cargar matrices A, B, C y D a formato de array de python
files = ['A.txt', 'B.txt', 'C.txt']
matrices = [] #se extraen los datos de las matrices en .txt y se convierten en array
for file in files:
    matrix = []
    with open(file, 'r') as f:
        for row in f:
            data = [float(x) for x in row.split(',')] 
            matrix.append(data)
    f.close()
    matrix = np.array(matrix)
    matrices.append(matrix)


A = matrices[0]
B = matrices[1]
C = matrices[2]
D = np.array(0)

#Se obtienen los autovalores y los autovectores
Autovalores, Autovectores=LA.eig(A)
#print('Autovalores = \n', Autovalores)

#print ('# Posicion, Autovalores =')
for index in range (len(Autovalores)):
    Autov = Autovalores[index]
    #print (index, Autov)




#SECCIóN 3.B:
    
#Seccionar "Autovalores" en sus partes real e imaginaria"   
ParteIm = Autovalores.imag
ParteReal = Autovalores.real




#SECCIóN 3.C:
#Se obtiene la frecuencia en modo oscilatorio de cada autovalor
for frec in Autovalores:
    frec = ParteIm/(2*np.pi)

#Se obtiene la razón de amortiguamiento del modo de oscilación de cada autovalor
for Chii in Autovalores:
    Chii = -(ParteReal/(np.sqrt(ParteReal**2+ParteIm**2)))

#print('\n\n\n')
#print ('# Posicion, Chi y frec, respectivamente:')
for index in range (len(Chii) and len(frec)):
    Chi = Chii[index]
    f = frec[index]
    
    #print (index, Chi, f)





#SECCIóN 3.E:

#Se crea una matriz de ceros de tipo complejo que se va a ir llenando de los vectores de participación
P=np.zeros((66,66),dtype='complex')

#La matriz de vectores derechos es "Autovectores"
#A continuación se obtiene la matriz de autovectores izquierdos "W"
W = LA.inv(Autovectores)
#print (W)


#Se hace un "for" para obtener la matriz de factores de participación "FP"
for k in range(66):
    for i in range (66):
        P[k,i]= Autovectores[k,i]*W[i,k]


#Se obtiene la matriz de Factores de participación en valores absolutos
Fp = abs(P)
#print('Factores de participación=\n', Fp)



#Se normaliza la matriz de Factores de participación
Fp_norm = Fp/Fp.max(axis=0)
#print (Fp_norm)




# SECCIóN 3.F:

#Se escogieron los Autovectores correspondientes a los 
# cinco modos de oscilacion de la seccion 3.c


#Los Autovectores se separan con respecto a los modos de oscilacion:


#Se crean los cinco vectores de las formas de modo que corresponden a cada uno de los modos de oscilación de la seccion 3.C
#Los vectores se llenan con los autovectores derechos correspondientes a la frecuencia de cada uno de los cuatro generadores


Vr1 = [0.0009038788919181075+0.00025944034983661475j,  0.0005633653793012544+0.0002907918079958743j, -0.0009825238170352332-0.0005089623896496397j,  -0.0009341174330890029-0.00042760368783339986j]
Vr2 = [-0.00027777584587706123-1.1300139638433226e-05j, 0.00033062604481911136+4.859870292271266e-05j, 0.0013319781348927933-0.00016234090936978598j, -0.0014593553436271685+4.266739989719568e-05j]
Vr3 = [-0.0013863209124746023-0.0022740270552820733j, 0.001359638744051245+0.002502078690737834j, 2.820052740995903e-05-0.00048632299032630146j, -6.112675357652567e-05+0.00028951411534228444j]
Vr4 = [-7.875065464279108e-05+0.0002355964203450399j,  -7.874391208040328e-05+0.0002355965990458009j, -7.872164104092265e-05+0.00023557814318521077j, -7.872019496977735e-05+0.0002355818841659522j]
Vr5 = [-4.08936258709919e-06-6.426226157811319e-06j,  -6.71486468005044e-07-5.576717184213659e-06j, -1.2045626073696395e-06-6.62929312261262e-06j, -5.4317634519734195e-08-5.003686697675431e-06j]


# Se crea un vector "Av" con todos los modos anteriores para más facil manipulación.
Av = [Vr1, Vr2, Vr3, Vr4, Vr5]




#hay que crear un bucle para trabajar más fácilmente con todos los modos, entonces se agrega un contador "k"

k=1


#Se crea un bucle para transformar el vector "Av" en un vector de magnitudes "Vfm"
for Vfm in Av:
    max_magnitude = 0
    for entry in Vfm:
        magnitude = abs(entry)
        if magnitude > max_magnitude:
            max_magnitude = magnitude


        
# Se "Vfm" con respecto a la norma más alta de cada una de sus columnas, ahora el vector "Vfm" es un vector normalizado con elementos de valores entre y -1, 0 y 1
    Vfm = [x/max_magnitude for x in Vfm]



#Se comienzan los comandos para graficar:

    plotted_vector = Vfm

# Graficar formas de modo
    re = [x.real for x in plotted_vector]
    im = [x.imag for x in plotted_vector]
    fig = plt.figure()
    labels = ['G1', 'G2', 'G3', 'G4']
    colors = ['b', 'g', 'r', 'y']
    plt.scatter(re, im, color=colors)
    for i in range(4):
        plt.text(re[i]-0.02, im[i]+0.02, labels[i], fontsize=9)
        plt.plot([0, re[i]], [0, im[i]], color = colors[i])
    plt.plot(0, 0, color='k', marker='o')
    plt.savefig(r"""Formas de modo """+str(k)+"""  sistema 4 generadores.pdf""",dpi=fig.dpi,facecolor='0.8')
    plt.show()

    k = k+1
        
    
        
        
        
        
