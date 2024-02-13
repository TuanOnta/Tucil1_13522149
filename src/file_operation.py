def readFile(filename):
    # Membaca file txt
    filename = "test/"+ filename  +".txt"# Gantilah 'nama_file.txt' dengan nama file yang sesuai
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Mengonversi isi file menjadi array
    array_data = []
    for line in lines:
        line = line.strip()
        if line:
            array_data.append(line.split())

    # Membaca buffer size dari file
    buffer_size = int(array_data[0][0])

    # Membaca ukuran matrix dari file
    matrix_width, matrix_height = int(array_data[1][0]), int(array_data[1][1])
    # Membaca matrix dari file
    matrix = [[0 for j in range(matrix_width)]for i in range (matrix_height)]

    for i in range(matrix_height):
        for j in range(matrix_width):
            matrix[i][j] = array_data[i+2][j]

    # Membaca banya sequence dari file
    number_of_sequence = int(array_data[matrix_height+2][0])

    # Mengkonversi sequence ke dalam array
    array_of_sequence = [array_data[matrix_height+3+i] for i in range(0, 2*number_of_sequence, 2)]
    array_of_value = [int(array_data[matrix_height+3+i][0]) for i in range(1, 2*number_of_sequence, 2)]

    return buffer_size, matrix_width, matrix_height, number_of_sequence, array_of_sequence, array_of_value, matrix

def saveFile(filename,value,sequence,array_of_coodinate,time):
    try:
        with open("test/" + filename + ".txt", 'w') as file:
            file.write(f"{value}\n")
            for i in sequence:
                file.write(f"{i} ")
            file.write("\n")
            for i in array_of_coodinate:
                file.write(f"{i}\n")
            file.write("\n")
            file.write(f"{time}ms\n\n")
        print(f"berhasil disimpan kedalam {filename}.txt")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")




