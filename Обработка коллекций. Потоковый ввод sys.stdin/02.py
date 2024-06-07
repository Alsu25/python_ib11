exc_list = []
classes_count = int( input( 'колич. классов: ' ) )
for i in range( classes_count ):
    exc_values = []
    n   = int( input('n = ') )
    for j in range(n):
        name, mark  = input('фамилия, оценка: ').split()
        exc_values.append( int(mark) == 5 )
    exc_list.append( any( exc_values ) )
if all( exc_list ):
    print('ДА')
else:
    print('НЕТ')