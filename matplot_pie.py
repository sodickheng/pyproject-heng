import matplotlib.pyplot as plt

# Data to plot
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [45, 30, 15, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title('Programming Language Popularity')
plt.show()
