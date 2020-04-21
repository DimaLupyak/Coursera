score = input("Enter Score: ")
try:
    score = float(score)    
except:
    print("Error: not number")
    quit()
    
if score > 1 or score < 0:
    print("Error:  value out of range")
    quit()
elif score >= 0.9:
    grade = "A"
elif score >= 0.8:
    grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"
else:
    grade = "F"

print(grade)