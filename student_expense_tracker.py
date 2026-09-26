print("STUDENT PERFORMANCE ANALYZER")
name = input("enter student name:")
maths = float(input("enter maths marks:"))
science = float(input("enter science marks:"))
english = float(input("enter english marks:"))
print("\n student name:", name)
print("maths:",maths)
print("science:",science)
print("english:",english)
total = maths + science + english 
average = total/3
percentage = (total/300)* 100
print(" \n total marks:", total)
print("average:" , average)
print("percentage:", percentage)
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
print ("grade:",grade)
if maths >= 35 and science >= 35 and english >= 35: 
    print(" result: PASS")
else:
    print("result: FAIL")
