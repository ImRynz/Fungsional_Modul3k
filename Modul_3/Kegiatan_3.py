random_list = ['Hello', 'Python', 'world', 'AI' , 105, 737, 412, 3.1, 2.7, 5.5]

data_float = list(filter(lambda x: isinstance(x, float), random_list))
data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_string = list(filter(lambda x: isinstance(x, str), random_list))

def map_int_to_dict(x):
    if x < 10:
        return {'ratusan': 0, 'puluhan': 0, 'satuan': x}
    elif x < 100:
        puluhan, satuan = divmod(x, 10)
        return {'ratusan': 0, 'puluhan': puluhan, 'satuan': satuan}
    else:
        ratusan, x = divmod(x, 100)
        puluhan, satuan = divmod(x, 10)
        return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

data = list(map(map_int_to_dict, data_int))

print("Data Float :")
print(data_float)
print("Data Int  :")
for item in data:
    print(item)
print("Data String :")
print(data_string)
