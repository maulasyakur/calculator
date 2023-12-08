from sys import argv

def main():
    # check for correct amount of cmd line args
    if len(argv) != 3:
        print("ERROR: This program needs two command line arguments to run, where first one is the input file and the second one is the output file!")
        return 1
    
    # check for correct input file
    try:
        with open(argv[1], "r") as finput:
            lines = finput.readlines()
    except:
        print(f"ERROR: There is either no such a file namely {argv[1]} or this program does not have permission to read it!")
        return 1
    
    foutput = open(argv[2], "w")

    for i in range(len(lines)):
        line = lines[i]
        # Skip empty lines
        if not line.strip():
            continue

        # Process non-empty lines
        line = line.strip()
        foutput.write(f"{line}\n")

        try:
            line = line.split()

            # checks whether the operation has two operands and an operator
            if len(line) != 3:
                raise ValueError("ERROR: Line format is erroneous!")

            # convert first operand
            try:
                operand1 = float(line[0])
            except ValueError:
                raise ValueError("ERROR: First operand is not a number!")

            # check for correct operator
            if line[1] in "+-*/":
                operator = line[1]
            else:
                raise ValueError("ERROR: There is no such an operator!")

            # convert second operand
            try:
                operand2 = float(line[2])
            except ValueError:
                raise ValueError("ERROR: Second operand is not a number!")

        except ValueError as e:
            foutput.write(f"{e}\n")
            continue

        # calculate operation
        if operator == '*':
            result = operand1 * operand2
        elif operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        else:
            result = operand1 / operand2
        
        # write down result on output file
        result = "{:.2f}".format(result)
        if i == len(lines) - 1:
            foutput.write(f"={result}")
        else:
            foutput.write(f"={result}\n")

    foutput.close()

main()