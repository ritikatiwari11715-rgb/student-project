print("STUDENT PERFORMANCE ANALYZER")

name = input("Enter student name: ")

maths = float(input("Enter maths marks: "))
science = float(input("Enter science marks: "))
english = float(input("Enter English marks: "))

print("\nStudent Name:", name)
print("Maths:", maths)
print("Science:", science)
print("English:", english)

total = maths + science + english
average = total / 3
percentage = (total / 300) * 100

print("\nTotal Marks:", total)
print("Average:", average)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if maths >= 35 and science >= 35 and english >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
    
