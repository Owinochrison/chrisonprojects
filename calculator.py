#Project: Modular Calculator
#Calculator 1: BMI

import math

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Test
weight = 69
height = 1.82
bmi = calculate_bmi(weight, height)
print(f"Weight : {weight} kg")
print(f"Height : {height} m")
print(f"BMI    : {bmi}")
print(f"Status : {bmi_category(bmi)}")

#Calculator 2: Step Goal Checker
def weekly_step_summary(steps_list, goal=8000):
    days_hit = len([s for s in steps_list if s >= goal])
    average = sum(steps_list) / len(steps_list)
    best = max(steps_list)
    worst = min(steps_list)

    return {
        "days_on_goal": days_hit,
        "total_days": len(steps_list),
        "average": round(average),
        "best_day": best,
        "worst_day": worst
    }

weekly = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
result = weekly_step_summary(weekly)

print("Step Summary:")
print(f"  Days on goal : {result['days_on_goal']}/{result['total_days']}")
print(f"  Average      : {result['average']} steps")
print(f"  Best day     : {result['best_day']} steps")
print(f"  Worst day    : {result['worst_day']} steps")

#Calculator 3: Calorie Estimate
#Estimates calories burned from walking. Uses approximately 0.04 calories per step.
import math

def estimate_calories(steps, calories_per_step=0.04):
    calories = steps * calories_per_step
    return math.floor(calories)

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
daily_cals = [estimate_calories(s) for s in weekly_steps]

print("Estimated daily calories burned from walking:")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day, cals in zip(days, daily_cals):
    print(f"  {day}: {cals} kcal")
print(f"  Total: {sum(daily_cals)} kcal")

#Calculator 4: Days on Protocol
def protocol_days_summary(steps_list, goal=8000):
    days_on_protocol = len([s for s in steps_list if s >= goal])
    total_days = len(steps_list)
    return days_on_protocol, total_days
steps_list = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
days_on_protocol, total_days = protocol_days_summary(steps_list)

print(f"Days on protocol: {days_on_protocol}/{total_days}")

import math
from datetime import date

# ---- DATA ----
client_name  = "James"
weight_kg    = 84
height_m     = 1.78
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
protocols    = ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"]
step_goal    = 8000

# ---- FUNCTIONS ----
def calculate_bmi(w, h):
    return round(w / (h**2), 1)

def bmi_category(bmi):
    if bmi < 18.5: return "Underweight"
    elif bmi < 25: return "Normal weight"
    elif bmi < 30: return "Overweight"
    else: return "Obese"

def weekly_step_summary(steps, goal=8000):
    return {
        "days_on_goal": len([s for s in steps if s >= goal]),
        "average": round(sum(steps) / len(steps)),
        "best": max(steps),
        "worst": min(steps)
    }

def estimate_calories(steps, rate=0.04):
    return math.floor(steps * rate)

def protocol_summary(plist):
    return {p: plist.count(p) for p in set(plist)}

# ---- REPORT ----
today = date.today().strftime("%d %B %Y")
bmi = calculate_bmi(weight_kg, height_m)
steps_report = weekly_step_summary(weekly_steps, step_goal)
total_cals = sum(estimate_calories(s) for s in weekly_steps)
proto_report = protocol_summary(protocols)

print("=" * 42)
print(f"  WEEKLY REPORT: {client_name.upper()}")
print(f"  Date: {today}")
print("=" * 42)
print(f"\nBODY")
print(f"  Weight : {weight_kg} kg")
print(f"  BMI    : {bmi} ({bmi_category(bmi)})")
print(f"\nSTEPS (Goal: {step_goal})")
print(f"  Days on goal : {steps_report['days_on_goal']}/7")
print(f"  Average      : {steps_report['average']} steps/day")
print(f"  Best day     : {steps_report['best']} steps")
print(f"  Worst day    : {steps_report['worst']} steps")
print(f"  Cals burned  : ~{total_cals} kcal")
print(f"\nPROTOCOL BREAKDOWN")
for p, d in proto_report.items():
    print(f"  {p}: {d} day(s)")
print("\n" + "=" * 42)

import pandas as pd

claims = pd.DataFrame({
    "claims_ID": [922,545,543,767,855],
    "claim_type": ["OP","DENTAL","OP","IP","OP"],
    "paid_amount": [3400,4400,3000,5000,7500],
    "claim_status": ["AUDITED","PAID","PAID","REJECTED","AUDITED"]
})
summary = claims.groupby("claim_type")["paid_amount"].agg(["sum", "mean", "count"]).round(2).reset_index()
print(summary)
print(claims["claim_type"].value_counts())


 #EXAMPLE

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian"],
    "steps":    [9200, None, 8100, 11000, None],
    "sleep_hr": [7.5, 8.0, None, 7.0, 9.0],
})

print("Original with NaN:")
print(df.to_string())

print("\nRows with any missing value:")
print(df[df.isna().any(axis=1)].to_string())

# Fill missing steps with the column mean
df["steps"] = df["steps"].fillna(df["steps"].mean())
df["sleep_hr"] = df["sleep_hr"].fillna(df["sleep_hr"].median())

print("\nAfter filling NaN:")
print(df.to_string())

#groupby in a Jua Kali Workshop

import pandas as pd

df = pd.DataFrame({
    "client":   ["Wanjiru", "Otieno", "Kamau", "Mwangi", "Njeri",  "Odhiambo", "Achieng", "Bett"],
    "item":     ["gate",    "grills", "frame", "gate",   "grills", "tank stand","frame",   "gate"],
    "material": ["mild steel","angle iron","hollow tube","mild steel","angle iron","mild steel","hollow tube","mild steel"],
    "price_kes":[28000, 14500, 9800, 32000, 12000, 18500, 11000, 29500],
    "status":   ["paid","paid","pending","paid","paid","pending","paid","paid"],
})

print("Revenue by material type:")
by_material = df.groupby("material")["price_kes"].agg(["sum","mean","count"]).round(0)
by_material.columns = ["total_kes", "avg_kes", "jobs"]
print(by_material.sort_values("total_kes", ascending=False).to_string())

print("\nPaid vs pending jobs:")
print(df["status"].value_counts())

print("\nAverage job value by status:")
print(df.groupby("status")["price_kes"].mean().round(0))

df["region"] = ["Nairobi","Kisumu","Nakuru","Nakuru","Nairobi","Nairobi","Kisumu","Nakuru"]
df1 = df.groupby(["region","material"])["price_kes"].mean().round(2)
print(df1)


import numpy as np

# Maize yield (90kg bags) per plot over a single season
yields = np.array([18, 22, 15, 31, 27, 19, 24, 12, 28, 21, 17, 25])
rainfall_mm = np.array([420, 510, 380, 620, 590, 440, 530, 310, 610, 490, 400, 560])

print("MAIZE YIELD ANALYSIS (90kg bags per plot)")
print(f"  Plots:        {len(yields)}")
print(f"  Total yield:  {np.sum(yields)} bags ({np.sum(yields) * 90:,} kg)")
print(f"  Mean:         {np.mean(yields):.1f} bags/plot")
print(f"  Median:       {np.median(yields):.1f} bags/plot")
print(f"  Std dev:      {np.std(yields):.1f}")
print(f"  Best plot:    {np.max(yields)} bags")
print(f"  Worst plot:   {np.min(yields)} bags")
print(f"  Top 25% (75th pctile): {np.percentile(yields, 75):.0f} bags")

print()
# Revenue at KES 2,800 per 90kg bag
revenue = yields * 2800
print("REVENUE (KES 2,800 per bag)")
print(f"  Total:        KES {np.sum(revenue):,}")
print(f"  Avg/plot:     KES {np.mean(revenue):,.0f}")

print()
# Correlation between rainfall and yield
corr = np.corrcoef(rainfall_mm, yields)[0, 1]
print(f"Rainfall vs yield correlation: {corr:.2f}")
print("(1.0 = perfect positive link, 0 = no link)")

#Project: Data Analysis Report
#Step 1: Load and Inspect
import numpy as np

# Maize yield (90kg bags) per plot over a single season
yields = np.array([18, 22, 15, 31, 27, 19, 24, 12, 28, 21, 17, 25])
rainfall_mm = np.array([420, 510, 380, 620, 590, 440, 530, 310, 610, 490, 400, 560])

print("MAIZE YIELD ANALYSIS (90kg bags per plot)")
print(f"  Plots:        {len(yields)}")
print(f"  Total yield:  {np.sum(yields)} bags ({np.sum(yields) * 90:,} kg)")
print(f"  Mean:         {np.mean(yields):.1f} bags/plot")
print(f"  Median:       {np.median(yields):.1f} bags/plot")
print(f"  Std dev:      {np.std(yields):.1f}")
print(f"  Best plot:    {np.max(yields)} bags")
print(f"  Worst plot:   {np.min(yields)} bags")
print(f"  Top 25% (75th pctile): {np.percentile(yields, 75):.0f} bags")

print()
# Revenue at KES 2,800 per 90kg bag
revenue = yields * 2800
print("REVENUE (KES 2,800 per bag)")
print(f"  Total:        KES {np.sum(revenue):,}")
print(f"  Avg/plot:     KES {np.mean(revenue):,.0f}")

print()
# Correlation between rainfall and yield
corr = np.corrcoef(rainfall_mm, yields)[0, 1]
print(f"Rainfall vs yield correlation: {corr:.2f}")
print("(1.0 = perfect positive link, 0 = no link)")


import pandas as pd
import numpy as np

# 28 days of SMP fitness log
data = {
    "day":      list(range(1, 29)),
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200,
                 8900, 10800, 9100, 11200, 7900, 10000, 9700,
                 9500, 10300, 8600, 11500, 8200, 9800, 10600,
                 9000, 10100, 8400, 10900, 7500, 9600, 10400],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0,
                 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5,
                 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5,
                 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8,
                 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9],
    "protocol": (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4),
    "cold_shower": ([True, True, False, True, True, True, True,
                     False, True, True, True, True, False, True] * 2),
    "bench_kg": [80, 82, 78, 85, 80, 83, 84,
                 81, 85, 80, 86, 79, 84, 83,
                 82, 86, 79, 88, 81, 85, 87,
                 82, 86, 80, 87, 79, 84, 86],
}
df = pd.DataFrame(data)

print(f"Shape: {df.shape}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nData types:")
print(df.dtypes)
print(f"\nMissing values: {df.isna().sum().sum()}")
print(f"\nFirst 3 rows:")
print(df.head(3).to_string())

#analysis of the above data
# High-performance days: 10k+ steps AND 7.5+ hours sleep
high_perf = df[(df["steps"] >=10000) & (df["sleep_hr"] >=7.5)] 
print(f"High-performance days: {len(high_perf)}/28")
print(high_perf)

# Protocol comparison
print("\nMetrics by fasting protocol:")
protocol_stats = df.groupby("protocol").agg(
    avg_steps=("steps", "mean"),
    avg_sleep=("sleep_hr", "mean"),
    avg_bench=("bench_kg", "mean"),
    avg_water=("water", "mean"),
    days=("day", "count")
).round(1)
print(protocol_stats)

#Step 3: NumPy Analysis

import pandas as pd
import numpy as np

data = {
    "day":      list(range(1, 29)),
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100, 11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800, 10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0, 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5, 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5, 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8, 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9],
    "protocol": (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4),
    "bench_kg": [80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86],
}
df = pd.DataFrame(data)

# High-performance days: 10k+ steps AND 7.5+ hours sleep
high_perf = df[(df["steps"] >= 10000) & (df["sleep_hr"] >= 7.5)]
print(f"High-performance days: {len(high_perf)}/28")

# Protocol comparison
print("\nMetrics by fasting protocol:")
protocol_stats = df.groupby("protocol").agg(
    avg_steps=("steps", "mean"),
    avg_sleep=("sleep_hr", "mean"),
    avg_bench=("bench_kg", "mean"),
    avg_water=("water", "mean"),
    days=("day", "count")
).round(1)
print(protocol_stats)

import pandas as pd
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100, 11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800, 10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400])
bench = np.array([80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86])
sleep = np.array([7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0, 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5, 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5, 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0])

print("=== 28-Day NumPy Analysis ===")
print(f"\nSteps:")
print(f"  Mean:        {np.mean(steps):,.0f}")
print(f"  Std dev:     {np.std(steps):,.0f}")
print(f"  25th pctile: {np.percentile(steps, 25):,.0f}")
print(f"  75th pctile: {np.percentile(steps, 75):,.0f}")
print(f"  Days 10k+:   {np.sum(steps >= 10000)}/28")

print(f"\nBench Press:")
print(f"  Mean:        {np.mean(bench):.1f} kg")
print(f"  Max:         {np.max(bench)} kg  (Day {np.argmax(bench)+1})")
print(f"  Trend:       {'increasing' if bench[-7:].mean() > bench[:7].mean() else 'flat/decreasing'}")

# Correlation: do more steps correlate with better bench?
corr = np.corrcoef(steps, bench)[0, 1]
print(f"\nCorrelation steps vs bench: {corr:.3f}")
print("Interpretation:", "positive relationship" if corr > 0.3 else "weak/no relationship")

#Project: Data Analysis Report
import pandas as pd
import numpy as np

# Data
steps_list = [9200, 10500, 8800, 11000, 7600, 9400, 10200, 8900, 10800, 9100, 11200, 7900, 10000, 9700, 9500, 10300, 8600, 11500, 8200, 9800, 10600, 9000, 10100, 8400, 10900, 7500, 9600, 10400]
sleep_list = [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0, 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5, 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5, 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0]
bench_list = [80, 82, 78, 85, 80, 83, 84, 81, 85, 80, 86, 79, 84, 83, 82, 86, 79, 88, 81, 85, 87, 82, 86, 80, 87, 79, 84, 86]
proto_list = (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4)
water_list = [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8, 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9]

df = pd.DataFrame({
    "day": list(range(1, 29)),
    "steps": steps_list, "sleep_hr": sleep_list,
    "bench_kg": bench_list, "protocol": proto_list, "water": water_list
})

steps = np.array(steps_list)
bench = np.array(bench_list)

W = 54
print("=" * W)
print("  SMP 28-DAY FITNESS ANALYSIS REPORT")
print("=" * W)

# Overall stats
print(f"\n  OVERALL METRICS")
print(f"  {'Days tracked:':<25} 28")
print(f"  {'Total steps:':<25} {steps.sum():,}")
print(f"  {'Avg daily steps:':<25} {steps.mean():,.0f}")
print(f"  {'Days hitting 10k:':<25} {(steps >= 10000).sum()}/28  ({(steps >= 10000).mean()*100:.0f}%)")
print(f"  {'Avg sleep:':<25} {np.mean(sleep_list):.1f} hrs")
print(f"  {'Bench press range:':<25} {bench.min()} to {bench.max()} kg")
print(f"  {'Bench press trend:':<25} +{bench[-7:].mean() - bench[:7].mean():.1f} kg (wk1 to wk4)")

# Week-by-week
print(f"\n  WEEKLY BREAKDOWN")
print(f"  {'Week':<8} {'Avg Steps':>12}  {'10k Days':>8}  {'Avg Bench':>10}")
print(f"  {'-'*44}")
for wk in range(4):
    s = steps[wk*7:(wk+1)*7]
    b = bench[wk*7:(wk+1)*7]
    hits = (s >= 10000).sum()
    print(f"  Week {wk+1:<3} {s.mean():>12,.0f}  {hits:>8}/7  {b.mean():>9.1f} kg")

# Protocol breakdown
print(f"\n  PROTOCOL COMPARISON")
proto_stats = df.groupby("protocol")[["steps", "sleep_hr", "bench_kg"]].mean().round(1)
for proto, row in proto_stats.iterrows():
    print(f"  {proto}: avg steps={row['steps']:,.0f}, sleep={row['sleep_hr']}h, bench={row['bench_kg']}kg")

# Top days
top3 = df.nlargest(3, "steps")
print(f"\n  TOP 3 STEP DAYS")
for _, row in top3.iterrows():
    print(f"  Day {int(row['day']):2d}: {int(row['steps']):,} steps  ({row['protocol']})")

print(f"\n{'=' * W}")