#Day 1 of Advent of Code 2023

#input is a calibration document
#need to extract a 2 digit number
    #consists of the first and last digit
    #digits can be stored as words

def trebuchet_part_two(input_file):
    file = open(input_file)
    sum = 0
    for x in file:
        #convert all words one to nine to numbers
        updated = replace_words(x)
        first = True
        cal = 0
        for char in updated:
            if char.isnumeric():
                curr = int(char)
                if first: #first digit
                    first = False
                    cal += curr * 10
        cal += curr #set calibrate value with last digit
        sum += cal #add to sum
    return sum

# wasn't really well explained so I found a cheesy solution
def replace_words(x):
    x = x.replace('one', 'o1e') 
    x = x.replace('two', 't2o') 
    x = x.replace('three', 't3e') 
    x = x.replace('four', 'f4r') 
    x = x.replace('five', 'f5e') 
    x = x.replace('six', 's6x')
    x = x.replace('seven', 's7n') 
    x = x.replace('eight', 'e8t') 
    x = x.replace('nine', 'n9e')
    return x

if __name__ == "__main__":
    print(trebuchet_part_two("input.txt"))
        