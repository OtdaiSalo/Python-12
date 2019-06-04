import re

machines = []
num = 0
regex = ".*((08\/Mar\/2004:((0[5-9])|(1[0-9])|(2[0-3])):([1-5][0-9]):((2[7-9])|([3-5][0-9])))|((09|10|11)\/Mar\/2004:(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9]))|(12\/Mar\/2004:((16:((2[1-9])|([3-5][0-9])):5[0-9])| (((1[7-9])|(2[0-3])):[0-5][0-9]:[0-5][0-9])))).*GET.*HTTP/.*401\s"


if __name__ == "__main__":
    with open("access_log") as file:
        for line in file:
            if re.search(regex, str(line)):
                num += 1

print(num)
