print('Hi,Welcome to the new system for devops')
print ('Whats your name?')
nome=input()

print ('Nice to meet you '+ nome + 'How old are you?')
idade=input()

print ('Nice! To continue our registration, which city do you live in?')
cidade=input()

print('Good ' + nome + ' whats is the number of your cpf')
cpf=input()

print('whats your gender?')
sexo=input()

print('we have complete your registration , your information is:')

print('Name:%s ' %  nome)
print('Age:%s ' % idade) 
print('CPF:%s ' % cpf)
print('City:%s ' % cidade)
print('Gender:%s ' % sexo)

print('If the data is correct , can we proceed with the registration? Yes or No ')
prosseguir=input()

if(prosseguir == 'yes'): 

	print('Cadastro concluido')

else:
        print('Lets redo registration')

 

