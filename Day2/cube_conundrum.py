#Day 2 of Advent of Code 2023

#playing a game that has 3 sets
#each set blue, green, and red cubes can be revealed
    #only 12 red cubes, 13 green cubes, 14 blue cubes
#if a set has more than any of these present the whole game is removed
#if all 3 sets are valid then add the game ID to sum
#return sum

def cube_conundrum(input_file):

    input = open(input_file)
    sum = 0

    for line in input: #for each line
        temp = line
        game_id = ""
        index = 5
        while temp[index].isnumeric(): #get game id
            game_id += temp[index]
            index += 1
        
        while index < len(temp) - 1: #go through line character by character
            num_cubes = ""
            while temp[index].isnumeric(): #get num cubes
                num_cubes += temp[index]
                index += 1
            if num_cubes != "" and int(num_cubes) > 12: #if bigger than 12 check to see if game is impossible
                color = temp[index+1]
                #any of below cases passing means break
                if (color == 'r') or (color == 'g' and int(num_cubes) > 13) or (color == 'b' and int(num_cubes) > 14):
                    break
            index+=1
        #if reached new line then add game_id
        if index == len(temp) - 1:
            sum += int(game_id)

    return sum
        
if __name__ == "__main__":
    print(cube_conundrum("input.txt"))            


