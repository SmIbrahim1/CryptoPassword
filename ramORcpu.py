
# 1st we need to create a huge number of value

# time
t = round(time.time() * 1000)
t = str(t)
t = t[8:]
# print(t)

# memory info
mi = psutil.virtual_memory()


# to extract only numbers from the memory info
def extract_num_from_string(string: str) -> str:
    # [0-9] is not always equivalent to \d. In python3, [0-9]
    # matches only 0123456789 characters, while \d matches [0-9]
    # and other digit characters,
    # for example Eastern Arabic numerals ٠١٢٣٤٥٦٧٨٩.
    return ''.join(re.findall('\d', string))


# taking a certain value form the memory info
memory = extract_num_from_string(f"{psutil.virtual_memory()}")
memory = memory[35:]
print(memory)
# taking ram usage percentage
ram = psutil.virtual_memory()[2]
# taking processor thread number
processor = psutil.cpu_count(logical=False)
# taking processor frequency
processorFrequency = psutil.cpu_freq().current

print(memory)
t = str((((int(memory) % int(t)) * int(memory)) * int(processor)) * len(str(t)) * int(processorFrequency))
print(t)
print(len(t))

# checking the number is even or not
randomNum = int(random.random() * 10)
if len(t) % 2 == 0:
    t = t
elif len(t) > len(t) / 2:
    t = str(t) + str(randomNum)
print(len(t))

# check the number is the number is

# 2nd we need to shift the bytes of the grip by random steps

# simply creating a 2d list
import numpy as np

value = [list(l) for l in list(np.reshape(list(t), (int(len(t) / 2), 2)))]
print(value)

# 3rd we need to take the row or the column to give the output
print(t)
