import csv
from sys import argv, exit

# sys.argv for command line arguments
if len(argv) != 3:
    print("Usage: missing command-line argument")
    exit(1)


STR_list = []
people = {}

# open data csv file, read contents into memeory, don't close file yet
csvfile = open(argv[1], "r")
dataObjects = csv.DictReader(csvfile)  # read file as dictionary format

for personObj in dataObjects:
    for key in personObj:
        if key == "name":
            name = personObj['name']
            if name not in people:
                # move name to the people object like this-> {"Bob":[]}
                people[name] = []
        else:
            # each key is string by default, needa convert to number
            repeats = int(personObj[key])
            people[name].append(repeats)  # add the numbers to each person
            if key in STR_list:
                pass  # save STRs to STR_list only if it's not there already
            else:
                STR_list.append(key)

# print(STR_list)  #now STR_list is like this -> ['AGATC', 'AATG', 'TATC']
# print(people)   #now people dict is liket his -> {"Bob": [4, 1, 5], "Alice": [...], ..}


# open DNA sequence, read contents into memeory
with open(argv[2], "r") as DNA_Seq:
    # it's a big string of random chars like this "AATCCGATTTCGCTAGGTCCT..."
    data = DNA_Seq.read()

STR_count = []  # count how many repeats of each subStr from DNA sequence file

for subStr in STR_list:  # check each str in the STR_list
    i = 0
    max_count = 0  # set max count for later use
    current_count = 0

    while i < len(data):  # make pointer to each checking char
        # find each subStr to match with each one from STR_list
        checkStr = data[i: i + len(subStr)]

        if checkStr == subStr:
            i += len(subStr)  # move on to the next subStr
            current_count += 1  # increase current count
            # find the max count, same as Math.max in JS
            max_count = max(max_count, current_count)

        else:
            i += 1  # move on to the next char
            current_count = 0  # reset to 0

    STR_count.append(max_count)  # add the max count of each subStr to the list

# print(STR_count)


# check to see if there's a match
for person in people:
    if people[person] == STR_count:  # is Bob's[4,1,5] same as STR_count[4,1,5] ?
        print(person)
        exit(0)
print("No match")


csvfile.close()
