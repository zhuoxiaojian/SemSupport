from django.test import TestCase

# Create your tests here.
import os
def get_count():
    count_path = "/repo/SMSInfo/count.txt"
    count_path_parent = "/repo/SMSInfo"
    count = "0"
    if os.path.exists(count_path_parent):
        if os.path.exists(count_path):
            f = open(count_path, "r")
            count = f.read()
            if count == "" or count is None:
                count = "0"
            f.close()
            pass
    else:
        os.mkdir(count_path_parent)
        f = open(count_path, "w")
        f.write("0")
        f.close()

    return count

def averageAssing(list, n):
    result = []
    remaider = len(list)%n
    number = len(list)//n
    offset = 0
    for i in range(0,n):
        value = None
        if remaider > 0:
            start_index = i*number+offset
            end_index = (i+1)*number+offset+1
            value = list[start_index:end_index]
            remaider = remaider-1
            offset = offset + 1

        else:
            start_index_e = i*number+offset
            end_index_e = (i+1)*number+offset
            value = list[start_index_e:end_index_e]
        result.append(value)
    return result
if __name__ == '__main__':
    print(averageAssing([], 4))
    print(get_count())