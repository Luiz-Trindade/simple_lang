# Linguagem de Programação simples.
# Interpretador criado por: Luiz Gabriel Magalhães Trindade.
# Distribuído sob a licença GPL3.
# Site da GPL3: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

version = """---------------------------------------------------------
-Simple Lang Version: 1.4
-Created by: Luiz Gabriel Magalhães Trindade.
-Distributed under GPL3 License: 
https://www.gnu.org/licenses/gpl-3.0.en.html#license-text
-Type an 'program_name' to execute!
----------------------------------------------------------
"""

help = """--------------------------
-How to use?
simple_lang program_name
--------------------------
"""

from sys import argv
from time import time
from os import system as S

instructions = []
memory = {}
sections = {}

program = ""

try:
    program = argv[1]
    if program == "-v":
        print(version)
    else:
        try:
            with open(program, "r") as file:
                instructions = [instructions.strip() for instructions in file]
        except:
            print(help)
except:
    print(version)

counter = int(0)
length = len(instructions)
while counter < length:
    command = instructions[counter].split(" ")

    if command[0] == "START":
        pass

    elif command[0] == "write":
        text = str(" ".join(command[1:]))
        text = text.replace("'", "")
        text = text.replace('"', '')
        text = text.replace("\\n", "\n")
        if "$" in text[0]:
            text = text.replace("$", "")
            try:
                print(str(memory[text]))
            except:
                print(float(memory[text]))
        else:
            print(text)

    elif command[0] == "string":
        var_name = command[1]
        content = " ".join(command[2:])
        content = content.replace("'", "")
        content = content.replace('"', '')
        memory[var_name] = content

    elif command[0] == "number":
        var_name = command[1]
        content = float(command[2])
        memory[var_name] = content

    elif command[0] == "read":
        var_name = command[1]
        content = input("")
        try:
            memory[var_name] = float(content)
        except:
            memory[var_name] = str(content)


    elif command[0] == "section":
        section_name = command[1]
        section_line = int(command[2])-1
        sections[section_name] = int(section_line)

    elif command[0] == "goto":
        #line_to_go = int(command[1])-1
        line_to_go = command[1]
        try:
            counter = sections[line_to_go]
            continue
        except:
            counter = int(line_to_go)-1
            continue

    elif command[0] == "math":
        value1 = float(memory[command[1]])
        operan = command[2]
        value2 = float(memory[command[3]])
        result = eval(f"{value1} {operan} {value2}")
        memory[command[4]] = float(result)

    elif command[0] == "comp":
        value1 = memory[command[1]]
        operan = command[2]
        value2 = memory[command[3]]
        line_to_jump = int(command[4])-1
        if operan == "==":
            if value1 == value2:
                counter = line_to_jump
                continue
        elif operan == "!=":
            if value1 != value2:
                counter = line_to_jump
                continue
        elif operan == "<":
            if value1 < value2:
                counter = line_to_jump
                continue
        elif operan == ">":
            if value1 > value2:
                counter = line_to_jump
                continue
        elif operan == "<=":
            if value1 <= value2:
                counter = line_to_jump
                continue
        elif operan == ">=":
            if value1 >= value2:
                counter = line_to_jump
                continue
        else: pass

    elif command[0] == "sleep":
        sleep(float(command[1]))

    elif command[0] == "SYSTEM":
        system_commands = str(" ".join(command[1:]))
        system_commands = system_commands.replace("'", "")
        system_commands = system_commands.replace('"', '')
        try:
            S(system_commands)
        except Exception as error :
            print(error)
            break
            
    elif command[0] == "END":
        break

    counter+=1
