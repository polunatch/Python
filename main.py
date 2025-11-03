print("Hello world!")


my_string = "Hello"
my_int = 42
my_float = 3.14
my_bool = True
my_list = [1, 2, 3]
my_dict = {"key": "value"}
my_tuple = (1, 2, 3)
my_none = None
print(5 > 3)
print("abc" == "abc")
print(True != False)
print([1,2] == [1,2])
print({"a":1} != {"b":2})
print((1,2) == (1,2))
num_str = str(125)
print(num_str, type(num_str))
message = 'Hi, my name is Python!'
message = message.replace('y', '0').replace('i', '1')
print(message)
split_test = 'This is a split test'
split_list = split_test.split()
print(split_list)
string_join = " ".join(split_list)
print(string_join)
print(len(string_join))
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)
index_of_6 = list_extend.index(6)
print(index_of_6)
print(len(list_append))
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())