grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sortedstud = sorted(students)
avgGrades = {}
for i in range(len(grades)):
    avgGrade = (sum(grades[i])/len(grades[i]))
    avgGrades[sortedstud[i]]=avgGrade
print(avgGrades)