"""
Start
get the numbers of sheets
sheets / 5
round the answer to next number
output result to user
End
"""


def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer,1)
    print("sheet is :", sheet)
    print("The answer is ", answer)
    print("rounded is: ", rounded)
    print("=============================================")
    return rounded

output = calculate(16)

print("the return statement is: ", output)

