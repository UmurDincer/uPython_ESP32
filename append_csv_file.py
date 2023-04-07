import random
from esp32 import Partition
import esp
import uos

filename = "csv_data_file.txt"

#  Get some statistics:
print("Available flash space: ", esp.flash_size()) # this will give the total amount of Flash available

partition = Partition(Partition.RUNNING)
print(partition.info()) #print out information about running flash partition on which you can store your files.

file_stats = uos.stat(filename)
print("File size before write: ", file_stats[6]) # the item at index 6 of the tupple contains total bytes in the file

#this loop will add 10 lines that contaion dummy comma-delimited data.
for x in range(10):
    random_value1 = random.randint(0, 50)
    random_value2 = random.randint(30, 150)
    random_value3 = random.randint(-300, 300)
    
    file = open(filename, "a") # append to the end of an existing file
    new_entry = "{},{},{}\n".format(random_value1, random_value2, random_value3)
    file.write(new_entry)
    file.close()
    
file_stats = uos.stat(filename)
print("File size after write: ", file_stats[6]) # the item at index 6 of the tupple contains total bytes in the file