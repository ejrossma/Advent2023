#Day 1 of Advent of Code 2023

#input is a calibration document
#need to extract a 2 digit number
    #consists of the first and last digit

def trebuchet(input_file):
    file = open(input_file)
    sum = 0
    for x in file:
        first = True
        cal = 0
        for char in x:
            if char.isnumeric():
                curr = int(char)
                if first: #first digit
                    first = False
                    cal += curr * 10
        cal += curr #set calibrate value with last digit
        sum += cal #add to sum
    return sum

if __name__ == "__main__":
    print(trebuchet("input.txt"))
        