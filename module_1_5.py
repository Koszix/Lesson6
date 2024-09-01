immutable_var = 1, 2, True, "String"
print(immutable_var)
#immutable_var[0] = 5 ; #Кортеж не поддерживает обращение по элиментам. Кортеж(корекция) = неизменяемая.
#print(immutable_var)
mutable_list = [1, 2, True, "String"]
print(mutable_list)
mutable_list[1] = 5
print(mutable_list) #Список можно изменить =)