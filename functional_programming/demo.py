# def is_square(x):
#     for sq in squares:
#         if sq == x:
#             return True
#         elif sq > x:
#             return False

# print(is_square(100), is_square(67))

# take 3 scores, determine overall percentage, determine grade (A*-D) and return message

overall = lambda hw, as_, ex: (hw + as_ + ex) * 100 // 175

grade = lambda percent: {100:'A*', 90:'A*', 80:'A', 70:'B', 60:'C', 50:'D'}.get(percent - (percent % 10), 'F')

gradecalc = lambda name, hw, as_, ex: name + " scored " + str(overall(hw, as_, ex)) + "%. " + name + "'s grade is " + grade(overall(hw, as_, ex))

def main():
    name = input("Enter name: ")
    hw = int(input("Enter homework score: "))
    as_ = int(input("Enter assessment score: "))
    ex = int(input("Enter exam score: "))
    print(gradecalc(name, hw, as_, ex))

main()