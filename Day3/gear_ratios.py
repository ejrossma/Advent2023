#Day 3 of Advent of Code 2023

#Schematic of an engine
#any number that is adjacent to a non-period symbol is a part for the engine
#return sum of all part numbers

def gear_ratios(input_file):
    input = open(input_file)
    schema = []
    sum = 0

    #take each line and put it into a list
    for line in input:
        schema.append(line)
    
    line_index = 0
    #loop through each character of each list
    for line in schema:
        char_index = 0
        line_len = len(line)
        while char_index < line_len - 1:
            #for each number loop through each digit of it and check all adjacent values to see if it should be added to sum
            num = ""
            
            keep_num = False
            while line[char_index].isnumeric():
                num += line[char_index]

                #up (only if index > 0) 
                if (line_index > 0 and is_symbol(schema[line_index - 1][char_index])):
                    keep_num = True
                #down (only if index < len(schema))
                if line_index < len(schema) - 1 and is_symbol(schema[line_index + 1][char_index]):
                    keep_num = True                
                #left (only if char_index > 0)
                if char_index > 0 and is_symbol(line[char_index-1]):
                    keep_num = True 
                #right (only if char_index < line_len)
                if char_index < line_len - 1 and is_symbol(line[char_index+1]):
                    keep_num = True
                #up left
                if char_index > 0 and line_index > 0 and is_symbol(schema[line_index - 1][char_index - 1]):
                    keep_num = True 
                #up right
                if char_index < line_len - 1 and line_index > 0 and is_symbol(schema[line_index - 1][char_index + 1]):
                    keep_num = True
                #down left
                if char_index > 0 and line_index < len(schema) - 1 and is_symbol(schema[line_index + 1][char_index - 1]):
                    keep_num = True
                #down right
                if char_index < line_len - 1 and line_index < len(schema) - 1 and is_symbol(schema[line_index + 1][char_index + 1]):
                    keep_num = True
                
                char_index += 1

            if keep_num:
                sum += int(num)
            char_index+=1
        line_index+=1
    return sum

#if not a . or number its a symbol
def is_symbol(char):
    if char != '.' and char != '\n' and not char.isnumeric():
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(gear_ratios("input.txt"))    
