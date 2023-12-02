# Linguagem de Programação simples.
# Interpretador criado por: Luiz Gabriel Magalhães Trindade.
# Distribuído sob a licença GPL3.
# Site da GPL3: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

from sys import argv

instructions = []
memory = {}

program = argv[1]
with open(program, "r") as file:
    content = file.readlines()
    for line in content:
        instructions.append(line.strip())


counter = int(0)
length = len(instructions)
while counter < length:
    command = instructions[counter].split(" ")
    #print(command)

    if command[0] == "START":
        pass

    elif command[0] == "write":
        text = str(" ".join(command[1:]))
        text = text.replace("'", "")
        text = text.replace('"', '')
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

    elif command[0] == "goto":
        line_to_go = int(command[1])-1
        counter = line_to_go
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
        

    elif command[0] == "END":
        break

    counter+=1
