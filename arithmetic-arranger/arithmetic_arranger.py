#FCC Python Exercise 1: Arithmetic formatter
# By Moira Campbell
"""
What need to be done?
Format and solve the text
1. Take each horizontal problem and extra the first operand, the operation symbol, and the second operand.
2. Detect the operation symbol and either save or add appropriately, save the result.
3. Format the problem correctly.
4. Print.
5. If answer=TRUE, print the stored answer.

"""
def arithmetic_arranger(problems, answer=None):
    line1 = ""
    line2 = ""
    op_store = ""
    divider = ""
    solution = ""
    solution_conc = ""
    Arranged_problems = ""

    if len(problems) > 5:
        raise Exception("Error: Too many problems.")


    for i in problems:
        problem_split = i.split()
        if len(problem_split[0]) > 4 or len(problem_split[2]) > 4:
            raise Exception("Error: Numbers cannot be more than four digits.")
        op_store = problem_split[1]
        line1 += f"  {problem_split[0].rjust(len(problem_split[2]))}    "
        line2_temp = f"{problem_split[1]} {problem_split[2].rjust(len(problem_split[0]))}"
        line2 += line2_temp + "    "
        divider_temp = "-"*len(line2_temp)
        try:
            if op_store == "+":
                solution = int(problem_split[0]) + int(problem_split[2])
            elif op_store == "-":
                solution = int(problem_split[0]) - int(problem_split[2])
            else:
                raise Exception("Error: Operator must be '+' or '-'.")
        except:
            print("Error: Numbers must only contain digits.")
            break

        solution_conc += "  " + str(solution) + "    " 
        divider += divider_temp + "    "


    Arranged_problems = f"{line1}\n{line2}\n{divider}\n"
    if answer == True:
        Arranged_problems += solution_conc
    return Arranged_problems
    #print(line1)
    #print(line2)
    #print(divider)
    #if answer == True:
     #   print(solution_conc)

# def arithmetic_arranger(problems, answer=None):
#     import re
#     operand1 = ""
#     operand2 = ""
#     divider = ""
#     operand_to_solve1 = ""
#     operand_to_solve2 = ""
#     operation = ""
#     answer = ""
#     solutions = ""
#     for i in problems
#         problem_split = re.split("\s", i, 1)
#         operand1 += problem_split[0].rjust(len(problem_split[1])+2)
#         operand2 += "  " + problem_split[1]
#         operand_to_solve1 = int(problem_split[0])
#         for num in problem_split[1]:
#             if num.isdigit() == True:
#                 divider += "-"
#                 operand_to_solve2 += num
#             elif num == "+":
#                 divider += "  "
#                 operation = "add"
#             elif num == "-":
#                 divider += "  "
#                 operation = "subtract"
#             else:
#                 divider += "  "
#         if operation == "add": 
#             answer = str(int(operand_to_solve1) + int(operand_to_solve2))
#         elif operation == "subtract":
#             answer = str(int(operand_to_solve1) - int(operand_to_solve2))
#         else:
#             print("Invalid operation :(")
#         solutions += answer.rjust(len(problem_split[1])+2)

#     print(operand1 + "\n" + operand2 + "\n" + divider)
#     print(solutions)


#     #Return Arranged_problems


arithmetic_arranger(["1 + 2", "444 - 33", "5555 + 6", "777 + 8888"], True)


