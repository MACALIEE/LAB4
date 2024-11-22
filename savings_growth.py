import matplotlib.pyplot as plt

def calculate_annual_growth(rate, years, annual_contribution=1200):
    savings = 0
    growth = []
    for year in range(1, years + 1):
        savings += annual_contribution
        savings *= (1 + rate / 100)
        growth.append(savings)
    return growth

years = 30
annual_contribution = 1200
rates = [1, 3, 5]

growth_data = {}
final_values = {}
for rate in rates:
    growth = calculate_annual_growth(rate, years, annual_contribution)
    growth_data[rate] = growth
    final_values[rate] = growth[-1]

print("Final Savings After 30 Years:")
for rate in rates:
    print(f"{rate}% Interest: ${final_values[rate]:,.2f}")

plt.figure(figsize=(10, 6))
for rate in rates:
    plt.plot(range(1, years + 1), growth_data[rate], label=f"{rate}% Interest Rate")

plt.title("Savings Growth Over 30 Years with Annual Compounding")
plt.xlabel("Years")
plt.ylabel("Total Savings ($)")
plt.legend()
plt.grid()
plt.show()

plt.close()