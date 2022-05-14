import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("star_with_gravity.csv")


mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()

plt.plot(radius, mass)

plt.title("Radius and Mass of the Star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass, gravity)

plt.title("Mass and Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()

plt.scatter(radius, mass)
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()
