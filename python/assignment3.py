student_names =['patricia', 'musa','phiona','myra']
student_marks =[80,56,78,90]

#print Patricia, Musa,phiona, and myra.
print (student_names[0])
print(student_names[1])
print(student_names[2])
print(student_names[3])

#Add Masha at the forth position.
student_names.insert(3,'masha')
print(student_names)
#Update the name phiona to "Phiona Aladina".
student_names[2] ='phiona aladina'
print(student_names)
#Print all the student names using a for loops.
for name in student_names:
    print(name)
#Calculate the total mark for the students mark variable.
total_mark = sum(student_marks)
print("Total Marks:",total_mark)
