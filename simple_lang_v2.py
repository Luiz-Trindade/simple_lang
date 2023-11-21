# Linguagem de Programação simples.
# Interpretador criado por: Luiz Gabriel Magalhães Trindade.
# Distribuído sob a licença GPL3.
# Site da GPL3: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

from sys import argv
from time import sleep
from colorama import Fore, Style

version = "Version: 2.0"
help = """HELP:
-usage: "./simple_lang program_name"

"""

instructions = []
memory = {}

program = argv[1]
if program == "-v":
    print(Fore.GREEN+version+Style.RESET_ALL)
elif program == "-h":
    print(Fore.YELLOW+help+Style.RESET_ALL)
else:
    try:
        with open(program, "r") as file:
            content = file.readlines()
            for i in content:
                instructions.append(i.strip())
    except Exception as error:
        print(Fore.RED+str(error)+Style.RESET_ALL)
        print("Type '-h' to get all commands usage.")

counter = 0
length = int(len(instructions)-1)

while counter <= length:
    command = instructions[counter].split(" ")

    if command[0] == "var":
        var_name = command[1]
        var_value = command[2:]
        try:
            memory[var_name] = float(var_value[0])
        except:
            memory[var_name] = str(var_value[0])

    elif command[0] == "read":
        var_name = command[1]
        print(memory[var_name])

    elif command[0] == "input":
        var_name = command[1]
        text_to_input = command[2:]
        content = input(" ".join(text_to_input)+" ")
        try:
            memory[var_name] = float(content[0:])
        except:
            memory[var_name] = str(content[0:])

    elif command[0] == "print":
        print(" ".join(command[1:]))

    elif command[0] == "goto":
        point_to = int(command[1])-1
        counter = point_to
        continue

    elif command[0] == "comp":
        name_1 = command[1]
        operan = command[2]
        name_2 = command[3]
        goto = int(command[4])-1
        if operan == "==":
            if memory[name_1] == memory[name_2]:
                counter = goto
                continue
        elif operan == "!=":
            if memory[name_1] != memory[name_2]:
                counter = goto
                continue
        elif operan == "<":
            if memory[name_1] < memory[name_2]:
                counter = goto
                continue
        elif operan == "<=":
            if memory[name_1] <= memory[name_2]:
                counter = goto
                continue
        elif operan == ">":
            if memory[name_1] > memory[name_2]:
                counter = goto
                continue
        elif operan == ">=":
            if memory[name_1] >= memory[name_2]:
                counter = goto
                continue

    elif command[0] == "math":
        value1 = command[1]
        operan = command[2]
        value2 = command[3]
        result = command[4]
        if operan == "+":
            x = float(memory[value1] + memory[value2])
            memory[result] = float(x)
        elif operan == "-":
            x = float(memory[value1] - memory[value2])
            memory[result] = float(x)
        elif operan == "*":
            x = float(memory[value1] * memory[value2])
            memory[result] = float(x)
        elif operan == "/":
            x = float(memory[value1] / memory[value2])
            memory[result] = float(x)
        elif operan == "**":
            x = float(memory[value1] ** memory[value2])
            memory[result] = float(x)
        elif operan == "%":
            x = float(memory[value1] % memory[value2])
            memory[result] = float(x)

    elif command[0] == "inc":
        var_name1 = command[1]
        var_name2 = command[2]
        memory[var_name1] += memory[var_name2]
    elif command[0] == "dec":
        var_name1 = command[1]
        var_name2 = command[2]
        memory[var_name1] += memory[var_name2]

    elif command[0] == "wait":
        sleep(float(command[1]))

    counter += 1
