resp_2 = input('Você quer fazer um calculo (s para sim e n para não): ')

while resp_2 == 's':

  n1 = int(input('Digite um numero: '))
  n2 = int(input('Digite outro numero: '))
  
  x = input('Digite o tipo de operação: (add para soma, sub para subtração, mult para multiplicação, div para divisão e exp para potência): ')
  
  if x == 'add':
    print('O resultado da soma é:', n1 + n2)
  
  if x == 'sub':
    print('O resultado da subtração é:', n1 - n2)
  
  if x == 'mult':
    print('O resultado da multiplicação é:', n1 * n2)
  
  if x == 'div':
    print('O resultado da divisão é:', n1 / n2)
  
  if x == 'exp':
    print('O resultado da potência é:', n1 ** n2)
  
  resp_2 = input('Deseja fazer um novo cálculo? ')
  if resp_2 == 'n':
    print('Obrigado por utilizar a MEGA CALCULADORA')