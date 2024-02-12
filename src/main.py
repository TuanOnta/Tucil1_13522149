import command
import file_operation
import time

print(f"Selamat datang \nsilahkan pilih input yang anda mau :")
print("1. Keyboard input")
print("2. File input")

masukan = int(input("SIlahkan masukan pilihan anda : "))
valid = False
while (valid == False):
    if(masukan == 1):
        buffer_size,matrix_width,matrix_height, number_of_sequence,array_of_sequence,array_of_value,matrix = command.keyboardInput()
        valid = True
    elif(masukan == 2):
        valid = True
        buffer_size,matrix_width,matrix_height, number_of_sequence,array_of_sequence,array_of_value,matrix = file_operation.readFile("dummy.txt")
    else:
        masukan = int(input(("Masukan anda tidak valid silahkan masukan kembali: ")))
        valid = False
print()
print()
print(f"besar buffer = {buffer_size}")
print(f"lebar matrix = {matrix_width}")
print(f"tinggi matrix = {matrix_height}")
print(f"matrix :")
for i in matrix:
    print(i)
print(f"number of sequence = {number_of_sequence}")
print(f"array of sequence = {array_of_sequence}")
print(f"array of value = {array_of_value}")

buffer_solutions = []
temp = []
boolean_matrix = [[False for j in range(matrix_width)]for i in range (matrix_height)]

start = time.time()
command.findAllSOlution(buffer_size,matrix_width,matrix_height,matrix,buffer_solutions, temp,boolean_matrix, 0,0)

best_seq, best_val = command.hitungPoint(number_of_sequence,array_of_sequence,array_of_value,buffer_solutions)

print("\n\n")
print(f"nilainya adalah  {best_val}")
print(f"sequence terbaik adalah : {best_seq}")
result = []
temp = []
command.findCoordinate(buffer_size,matrix_width,matrix_height,matrix,result, temp,best_seq,0,0)
end = time.time()
duration = round((end - start)*10**3)

print(f"koordinat dari sequencenya adalah ")
for i in result:
    print(i)
print()
print()
print(f"{duration}ms")

masukan = input("Apakah anda ingin menyimpan solusi? (y/n)")
valid = False
while(valid == False):
    if (masukan == 'y'):
        valid = True
        # simpan file
    elif(masukan == 'n'):
        valid = True
        # do nothing
    else :
        masukan = input(("Masukan anda tidak sesuai silahkan masukan kembali: "))
        