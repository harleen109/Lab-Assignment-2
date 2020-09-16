"""
Start
get the numbers of sheets
sheets / 5
round the answer to next number
output result to user
End
"""
import math 

# input: sheet

def calculate(sheet):
# step 1
    answer = sheet / 5
    rounded = math.ceil(answer)
# Step 2
    print("sheet is :", sheet)
    print("The answer is ", answer)
    print("rounded is: ", rounded)
    print("=============================================")
 # outpput: number of stamps needed
    return rounded

output = calculate(16)

print("The number of stamps required is: ", output)

