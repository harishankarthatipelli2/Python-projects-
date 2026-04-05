# ---------------- SETUP ---------------- #
import matplotlib.pyplot as plt
import pandas as pd

# ---------------- SAMPLE DATA ---------------- #
data = [
    {"date": "2026-04-01", "category": "Food", "amount": 120, "description": "Lunch"},
    {"date": "2026-04-02", "category": "Transport", "amount": 50, "description": "Bus"},
    {"date": "2026-04-03", "category": "Food", "amount": 200, "description": "Dinner"},
    {"date": "2026-04-05", "category": "Shopping", "amount": 500, "description": "Clothes"},
    {"date": "2026-05-01", "category": "Food", "amount": 150, "description": "Snacks"},
    {"date": "2026-05-02", "category": "Transport", "amount": 70, "description": "Auto"},
]

df = pd.DataFrame(data)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# ---------------- VIEW DATA ---------------- #
print("📋 Expense Data:")
display(df)

# ---------------- TOTAL SPENDING ---------------- #
total = df["amount"].sum()
print("\n💰 Total Spending:", total)

# ---------------- CATEGORY ANALYSIS ---------------- #
category_data = df.groupby("category")["amount"].sum()

print("\n📊 Category-wise Spending:")
print(category_data)

# ---------------- MONTHLY ANALYSIS ---------------- #
df["month"] = df["date"].dt.to_period("M")
monthly_data = df.groupby("month")["amount"].sum()

print("\n📅 Monthly Spending:")
print(monthly_data)

# ---------------- PIE CHART ---------------- #
plt.figure()
category_data.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category-wise Spending")
plt.ylabel("")
plt.show()

# ---------------- LINE CHART ---------------- #
plt.figure()
monthly_data.plot(marker='o')
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.show()
