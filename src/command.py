import file_operation

def findAllSOlution(buffer_size,matrix_width,matrix_height,matrix,buffer_solutions, temp,boolean_matrix, number_of_elmt,axis):
    if number_of_elmt == buffer_size :
        buffer_solutions.append(list(temp))
    elif number_of_elmt == 0 :
        for i in range(matrix_width):
            if(boolean_matrix[0][i] == False):
                boolean_matrix[0][i] = True
                findAllSOlution(buffer_size,matrix_width,matrix_height,matrix,buffer_solutions,[matrix[i][0]],boolean_matrix,number_of_elmt+1,i)
                boolean_matrix[0][i] = False
    elif number_of_elmt%2 == 1:
        for i in range(matrix_height):
            if(boolean_matrix[i][axis] == False):
                boolean_matrix[i][axis] = True
                temp.append(matrix[i][axis])
                findAllSOlution(buffer_size,matrix_width,matrix_height,matrix,buffer_solutions,temp,boolean_matrix,number_of_elmt+1,i)
                temp.pop()
                boolean_matrix[i][axis] = False
                
    else:
        for i in range(matrix_width):
            if(boolean_matrix[axis][i] == False):
                boolean_matrix[axis][i] = True
                temp.append(matrix[axis][i])
                findAllSOlution(buffer_size,matrix_width,matrix_height,matrix,buffer_solutions,temp,boolean_matrix,number_of_elmt+1,i)
                temp.pop()
                boolean_matrix[axis][i] = False

def is_subarray(subarray, array):
    # Mendapatkan panjang array dan subarray
    len_array = len(array)
    len_subarray = len(subarray)

    # Mengecek apakah panjang subarray lebih kecil atau sama dengan panjang array
    if len_subarray > len_array:
        return False

    # Melakukan iterasi untuk mencari subarray yang sama dengan array
    for i in range(len_array - len_subarray + 1):
        if array[i:i + len_subarray] == subarray:
            return True

    # Jika tidak ditemukan subarray yang sama
    return False

def hitungPoint(number_of_sequence,array_of_sequence,array_of_value,buffer_solutions):
    best_seq = None
    best_val = 0
    for sol in  buffer_solutions:
        val = 0
        for i in range (number_of_sequence):
            if is_subarray(array_of_sequence[i],sol):
                val += array_of_value[i]
        if(val > best_val):
            best_seq = sol
            best_val = val
    return best_seq, best_val

def findCoordinate(buffer_size,matrix_width,matrix_height,matrix,result, array_of_coor,sequence,index_elmt,axis):
    if len(array_of_coor) == buffer_size:
        result.clear()
        for el in array_of_coor:
            result.append(el)
    elif index_elmt== 0:
        array_of_coor = []
        for i in range(matrix_width):
            if matrix[0][i] == sequence[0]:
                coor = (i+1,1)
                array_of_coor.append(coor)
                findCoordinate(buffer_size,matrix_width,matrix_height,matrix,result,array_of_coor,sequence,index_elmt+1,i)
                array_of_coor.pop()
    elif index_elmt % 2 == 1 and index_elmt <= buffer_size:
        for i in range(matrix_height):
            if matrix[i][axis] == sequence[index_elmt]:
                coor = (axis+1,i+1)
                array_of_coor.append(coor)
                findCoordinate(buffer_size,matrix_width,matrix_height,matrix,result,array_of_coor,sequence,index_elmt+1,i)
                array_of_coor.pop()
    elif index_elmt % 2 == 0 and index_elmt <= buffer_size:
        for i in range(matrix_width):
            if matrix[axis][i] == sequence[index_elmt]:
                coor = (i+1,axis+1)
                array_of_coor.append(coor)
                findCoordinate(buffer_size,matrix_width,matrix_height,matrix,result,array_of_coor,sequence,index_elmt+1,i)
                array_of_coor.pop()

def keyboardInput():
    buffer_size = int(input("Masukan besar buffer : "))
    matrix_height = int(input("Masukan Tinggi matrix: "))
    matrix_width = int(input("Masukan lebar matrik: "))
    matrix = []
    # Membaca input matriks dari pengguna
    print("Masukan matrix (Setiap elemen dipisahkan dengan spasi)")
    for i in range (matrix_height):
        matrix_input = input()
        matrix.append(list(map(str, matrix_input.split())))  

    number_of_sequence = int(input("Masukan banyak sequence yang anda mau: "))
    
    list_of_sequence = []
    list_of_value = []
    for i in range(number_of_sequence):
        seq = input(f"masukan sequence ke-{i+1}: ")
        list_of_sequence.append(list(map(str,seq.split())))
        val = int(input("Masukan nilai yang anda mau dari sequence diatas: "))
        list_of_value.append(val)
    
    return buffer_size,matrix_width,matrix_height, number_of_sequence,list_of_sequence,list_of_value,matrix


