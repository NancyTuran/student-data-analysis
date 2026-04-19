import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

# 📋 Table print
print("\nStudent Data Table:\n")
print(df)

# 📊 Graph + Table display
fig, ax = plt.subplots()

# Graph
ax.bar(df["Name"], df["Marks"])

# Table add karna graph ke niche
table = plt.table(
    cellText=df.values,
    colLabels=df.columns,
    loc='bottom'
)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")

# Layout adjust (important)
plt.subplots_adjust(left=0.2, bottom=0.3)

plt.show()