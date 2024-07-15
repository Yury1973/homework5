immutable_var = 1, 'nut', True, 8
print('Immutable tuple:', immutable_var)
# immutable_var[2] = 15  # Кортеж - неизменяемая структура, которая хранит только ссылку на список, а не сам список
mutable_list = [1, 'nut', True, 8]
mutable_list[1] = 34
mutable_list.append('potato')
print('Mutable list:', mutable_list)
