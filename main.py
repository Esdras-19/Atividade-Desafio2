from moda import moda
from media import media
from mediana import mediana
from desvio import desvio

portugues=[]
matematica=[]
fisica=[]
quimica=[]
ingles=[]

def nota():
 print('''Escolha a disciplina desejada:

 1-Português
 2-Matemática
 3-Física
 4-Química
 5-Inglês

 ''')

 escolha=int(input('>>'))
 

 if escolha==1:
    print('Digite as notas da disciplina de Português:')
    nota_portugues1=float(input('>>'))
    nota_portugues2=float(input('>>'))
    nota_portugues3=float(input('>>'))
    nota_portugues4=float(input('>>'))

    portugues.append(nota_portugues1)
    portugues.append(nota_portugues2)
    portugues.append(nota_portugues3)
    portugues.append(nota_portugues4)

     
    print('Notas de Português:',portugues)
    moda(portugues)
    media(portugues)
    mediana(portugues)
    desvio(portugues)
    valor_minimo=min(portugues)
    valor_maximo=max(portugues) 
    print('Menor nota:',valor_minimo)
    print('Maior nota:', valor_maximo)  

 elif escolha==2:
    print('Digite as notas da disciplina de Matemática:')
    nota_matematica1=float(input('>>'))
    nota_matematica2=float(input('>>'))
    nota_matematica3=float(input('>>'))
    nota_matematica4=float(input('>>'))

    matematica.append(nota_matematica1)
    matematica.append(nota_matematica2)
    matematica.append(nota_matematica3)
    matematica.append(nota_matematica4)

    print('Notas de Matemática:',matematica)
    moda(matematica)
    media(matematica)
    mediana(matematica)
    desvio(matematica) 
    valor_minimo1=min(matematica)
    valor_maximo1=max(matematica) 
    print('Menor nota:',valor_minimo1)
    print('Maior nota:', valor_maximo1) 

   

 elif escolha==3:
      print('Digite as notas da disciplina de Física:')
      nota_fisica1=float(input('>>'))
      nota_fisica2=float(input('>>'))
      nota_fisica3=float(input('>>'))
      nota_fisica4=float(input('>>'))

      fisica.append(nota_fisica1)
      fisica.append(nota_fisica2)
      fisica.append(nota_fisica3)
      fisica.append(nota_fisica4)

      print('Notas de Física:',fisica)
      moda(fisica)
      media(fisica)
      mediana(fisica)
      desvio(fisica) 
      valor_minimo2=min(fisica)
      valor_maximo2=max(fisica) 
      print('Menor nota:',valor_minimo2)
      print('Maior nota:', valor_maximo2) 

 elif escolha==4:
    print('Digite as notas da disciplina de Química:')
    nota_quimica1=float(input('>>'))
    nota_quimica2=float(input('>>'))
    nota_quimica3=float(input('>>'))
    nota_quimica4=float(input('>>'))

    quimica.append(nota_quimica1)
    quimica.append(nota_quimica2)
    quimica.append(nota_quimica3)
    quimica.append(nota_quimica4)

    print('Notas de Química:',quimica)
    moda(quimica)
    media(quimica)
    mediana(quimica)
    desvio(quimica) 
    valor_minimo3=min(quimica)
    valor_maximo3=max(quimica) 
    print('Menor nota:',valor_minimo3)
    print('Maior nota:', valor_maximo3) 



 elif escolha==5:
      print('Digite as notas da disciplina de Inglês:')
      nota_ingles1=float(input('>>'))
      nota_ingles2=float(input('>>'))
      nota_ingles3=float(input('>>'))
      nota_ingles4=float(input('>>'))

      ingles.append(nota_ingles1)
      ingles.append(nota_ingles2)
      ingles.append(nota_ingles3)
      ingles.append(nota_ingles4)

      print('Notas de Inglês:',ingles)
      moda(ingles)
      media(ingles)
      mediana(ingles)
      desvio(ingles) 
      valor_minimo4=min(ingles)
      valor_maximo4=max(ingles) 
      print('Menor nota:',valor_minimo4)
      print('Maior nota:', valor_maximo4) 

else:
    print('Digite uma opção válida')

nota()
  

