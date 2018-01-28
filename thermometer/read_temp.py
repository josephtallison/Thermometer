import time
import datetime

temp_file_output = "/sys/bus/w1/devices/28-000008c5790a/w1_slave"


class NoTempValueException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


def read_temp():
    with open(temp_file_output) as f:
        first_line = f.readline().strip()
        if first_line[-3:] == "YES":
            temp_line = f.readline().strip()
            raw_temp = temp_line.split("=")[-1]
            return float(raw_temp)
        else:
            raise NoTempValueException()

def convert_celcius_to_fahrenheit(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp


if __name__ == "__main__":
    while True:
        try:
            raw_temp = read_temp()
        except NoTempValueException:
            print("Missing Temp")
            continue
        c_temp = raw_temp/1000
        f_temp = convert_celcius_to_fahrenheit(c_temp)
        print(datetime.datetime.now().time(), round(f_temp, 1))
        time.sleep(0.2)
