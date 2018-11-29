def get_summ(num_one, num_two):
    summ = int(num_one) + int(num_two)
    print('result is: ' + str(summ))

try:
    get_summ(input('please, enter 1st value: '),input('please, enter 2nd value: '))
except ValueError:
    print('Bad value')