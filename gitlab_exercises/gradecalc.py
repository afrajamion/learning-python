'''
Create an application which asks the user for an input for a maths mark, a chemistry mark and a physics mark.
Add the marks together, then work out the overall percentage. And print it out to the screen.
If the percentage is below 40%, print “You failed”
If the percentage is 40% or higher, print “D”
If the percentage is 50% or higher, print “C”
If the percentage is 60% or higher, print “B”
If the percentage is 70% or higher, print “A”
'''

def grade_calc(maths, chem, phys):
    percent = (maths + chem + phys)/3
    bound = {70: 'A', 60: 'B', 50: 'C', 40: 'D'}
    for x in bound:
        if percent >= x:
            grade = bound[x]
            return f"You scored {percent}%. Your grade is {grade}"
            break
        else:
            continue
    else:
        return f"You scored {percent}%. Sorry, you did not pass"


u_math = float(input("Please enter a maths mark out of 100: "))
u_chem = float(input("Please enter a chemistry mark out of 100: "))
u_phys = float(input("Please enter a physics mark out of 100: "))
if u_math > 100 or u_chem > 100 or u_phys > 100:
    print("Invalid marks entered!")
else:
    print(grade_calc(u_math, u_chem, u_phys))
