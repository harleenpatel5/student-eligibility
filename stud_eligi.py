#1.Take user input for name,age,marks
#2.represent min passing marks=40
#bonus marks=5
#final marks = marks + bonus marks
#has passed = final marks >= pass marks
#is eligible = age >= 18 and has passed
#display - user result, student result, name, age, original marks, bonus marks, final marks, passed or not, eligibility

name=input("Enter name:")
age=int(input("Enter age:"))    
marks=int(input("Enter marks:"))
pass_marks=40
bonus_marks=5
final_marks = marks + bonus_marks
has_passed = final_marks >= pass_marks
is_eligible = age >= 18 and has_passed
print("User Result:")
print("Student Result:")
print("Name:", name)
print("Age:", age)
print("Original Marks:", marks)
print("Bonus Marks:", bonus_marks)
print("Final Marks:", final_marks)
if has_passed:
    print("Passed: Yes")    
else:
    print("Passed: No")
print("Eligible: ", is_eligible)