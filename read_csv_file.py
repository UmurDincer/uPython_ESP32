
filename = "csv_data_file.txt"

i = 1

with open(filename, 'r') as file:
    for line in file:
        line = line.rstrip('\n') # remove any '\n'
        data = line.split(',')
        print("Line: ", len(line), "Raw: ", line)
        if len(line) > 1:
            csv_row = "Row: {}\nValue 1: {}\nValue 2: {}\nValue 3: {}\n".format(i, data[0],data[1],data[2])
            print(csv_row)
        i = i + 1
file.close()