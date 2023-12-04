#Day 2 of Advent of Code 2023

#each set blue, green, and red cubes can be revealed
#find smallest amount of each color that is revealed
#multiply each lines minimums together and add to sum
#return sum

def cube_conundrum_part_two(input_file):

    input = open(input_file)
    sum = 0

    for line in input: #for each line
        temp = line
        index = 5
        min_r = min_g = min_b = 0
        
        while index < len(temp) - 1: #go through line character by character
            num_cubes = ""
            while temp[index].isnumeric(): #get num cubes
                num_cubes += temp[index]
                index += 1
            if num_cubes != "": #check if num > min for that color
                color = temp[index+1]
                #any of below cases passing means break
                if color == 'r' and int(num_cubes) > min_r:
                    min_r = int(num_cubes)
                elif color == 'g' and int(num_cubes) > min_g:
                    min_g = int(num_cubes)
                elif color == 'b' and int(num_cubes) > min_b:
                    min_b = int(num_cubes)
            index += 1
        #if reached new line then add game_id
        if index == len(temp) - 1:
            sum += (min_b * min_g * min_r)

    return sum
        
if __name__ == "__main__":
    print(cube_conundrum_part_two("input.txt"))            


