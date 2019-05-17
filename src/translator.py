def look_number(line):
    counter = 1
    sol = int(line[0])
    line = line[1:]
    while line != "":
        if line[0].isdigit():
            sol = (sol * 10) + int(line[0])
            line = line[1:]
            counter += 1
        else:
            break
    return [sol, counter]


def translate(original_text, sol_name="Solution"):
    file_out = open(sol_name + ".txt", "w")

    lines = original_text.splitlines()
    sol = ""
    numbers = []
    for line in lines:
        while line != "":
            if line[0].isdigit():
                sol += "%d"
                numbers.append(look_number(line)[0])
                line = line[look_number(line)[1]:]
            elif line[0] == "\"":
                sol += "\\" + line[0]
                line = line[1:]
            elif line[0] == "/":
                sol += "\\"
                line = line[1:]
            else:
                sol += line[0]
                line = line[1:]

        if sol == " ":
            sol = "\\n"
            continue
        sol += "\\n\""
        for number in numbers:
            sol += ", " + str(number)
        file_out.write("printf(\"" + sol + ");\n")
        numbers = []
        sol = ""
    file_out.close()
