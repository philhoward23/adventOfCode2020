#part 1
#find integers with sum 2020
day1input=open("input.txt")
input = day1input.readlines()
input_ints = [int(x.strip()) for x in input]


dup=False


for i, x in enumerate(input_ints):
    for j, y in enumerate(input_ints[i+1:]):
        print(i,j,x,y,x+y)
        if x+y == 2020:
            print(x,y,x*y)
            break
    if x+y == 2020:
        print(i,j,x,y,x*y)
        break
#921504

#part 2
#find 3 integers that sum to 2020
for i, x in enumerate(input_ints):
    for j, y in enumerate(input_ints[i+1:]):
        for k, z in enumerate(input_ints[j+1:]):
            print(x,y,z,x+y+z)
            if x+y+z == 2020:
                print(x,y,z,x*y*z)
                break
        if x+y+z == 2020:
            print(x,y,z,x*y*z)
            break
    if x+y+z == 2020:
        print(i,j,k,x,y,z,x*y*z)
        break
#195700142