team1 = "Мастера кода"
team2 = "Волшебники данных"
team1_members = 5
team2_members = 6
team1_score = 40
team2_score = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print("В финал выходят 2 команды: %s и %s!" % (team1, team2))
print("В команде Мастера кода участников: %d!" % team1_members)
print("В команде Волшебники данных участников: %d!" % team2_members)
print("Итого сегодня в командах участников: %d и %d!" % (team1_members, team2_members))
print("Команда Волшебники данных решила задач: {score}!".format(score=team2_score))
print("Волшебники данных решили задачи за {time} секунд!".format(time=team2_time))
print(f"Команды решили {team1_score} и {team2_score} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")