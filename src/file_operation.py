def readFile(filename):
    # Membaca file txt
    file_path = 'dummy.txt'  # Gantilah 'nama_file.txt' dengan nama file yang sesuai
    with open(file_path, 'r') as file:
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
    array_of_sequence = [0 for i in range(number_of_sequence)]
    array_of_value = [0 for i in range(number_of_sequence)]

    for i in range(number_of_sequence):
        if(i % 2 == 0):
            array_of_sequence[i] = array_data[matrix_height+3+i]
        else:
            array_of_value[i] = int(array_data[matrix_height+3+i][0])

    return buffer_size,matrix_width,matrix_height, number_of_sequence,array_of_sequence,array_of_value,matrix




