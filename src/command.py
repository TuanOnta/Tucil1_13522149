import file_operation


buffer_size,matrix_width,matrix_height, number_of_sequence,array_of_sequence,array_of_value,matrix = file_operation.readFile("dummy.txt")

print(f"buffer size = {buffer_size}")
print(f"lebar matrix = {matrix_width}")
print(f"tinggi matrix = {matrix_height}")
print(f"matrix = {matrix}")
print(f"number of sequence = {number_of_sequence}")
print(f"array of sequence = {array_of_sequence}")
print(f"array of value = {array_of_value}")

