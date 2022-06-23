employee_name = input('Digite o seu nome por favor: ')
explict_employee_name = input('O seu nome é {} (S/n)? '.format(employee_name))
if explict_employee_name == 'S':
    print('\nSeja muito bem vindo {}!\n'.format(employee_name))
else:
    print('Por favor, digite novamente {}!'.format(employee_name))
