import re

def arithmetic_arranger(problems, answer=None):
    operand1 = ""
    operand2 = ""
    operand2_justified = ""
    divider = ""
    for i in problems:
        problem_split = re.split("\s", i, 1)
        #operand1 += "    " + problem_split[0]
        operand1 += problem_split[0].rjust(len(problem_split[0])+4)
        #operand2 += "  " + problem_split[1]
        operand2 += problem_split[1]
        operand2_justified += operand2[0] + "##" + operand2[1:] + "##"
    for num in operand2:
        if num.isdigit() == True:
            divider += "-"
        else:
            divider += " "

    print(operand1 + "\n" + operand2_justified + "\n" + divider)


    #return arranged_problems


arithmetic_arranger(["1 + 2", "33 - 44", "555 + 66", "777 + 8888"])



