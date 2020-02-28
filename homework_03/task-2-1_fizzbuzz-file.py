import sys

read_list        = []
fizz        = 0
buzz        = 0
n           = 0

filename_r = sys.argv[1]
filename_w = sys.argv[2]

#read from file
f_r = open(filename_r, 'r')

for line in f_r:
    read_list.append(line)
f_r.close()


f_w = open(filename_w, 'w')

#fizz buzz function
for i in range(0, len(read_list) - 1):
    current_line     = read_list[i].split()
    fizz             = int(current_line[0])
    buzz             = int(current_line[1])
    n                = int(current_line[2])
    result_line_list = []
    result_line_str  = ''

    for j in range(1, n + 1):
        if (not j % fizz and not j % buzz):
            result_line_list.append('FB')

        elif (not j % fizz):
            result_line_list.append('F')

        elif (not j % buzz):
            result_line_list.append('B')

        else:
            result_line_list.append(n)

    #write to file
    f_w.write('fizz = ' + str(fizz) + '; buz = ' + str(buzz) + '; n = ' + str(n) + '\n')
    f_w.write('Result: ' + ' ')
    f_w.write(result_line_str.join(str(e) for e in result_line_list) + '\n\n')

f_w.close()