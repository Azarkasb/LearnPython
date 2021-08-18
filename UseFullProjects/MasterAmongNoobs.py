'''Creating a simple pie chart'''
# AZ
import matplotlib.pyplot as plt
humans = [1, 2, 1, 7]
level = ['Legendary\nGrandMaster', 'Specialist', 'Pupil', 'newbi']
exp = [0.2, 0.0, 0.0, 0.0]
plt.pie(humans, labels=level, startangle=0, explode=exp,
        shadow=True, colors=['darkred', 'c', 'g', 'gray'])

plt.show()
