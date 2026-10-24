# chrisonowino
Chrison Owino | Python Developer | Automation & AI Tools

Building practical tools that solve actual problems. Based in Nairobi, Kenya.

What I Build
Data pipelines and automation scripts in Python
REST APIs with FastAPI and Flask
Machine learning tools for fitness and performance tracking
Browser-based tools with JavaScript and the Fetch API
Current Projects
smp-tracker: Daily performance tracker with ML-powered coaching
api-dashboard: Multi-endpoint data dashboard with pandas reports
browser-coach: Client-side AI coaching tool in JavaScript
Stack
Python • FastAPI • Pandas • scikit-learn • JavaScript • Git • Supabase

**PROJECTS**

SMP Tracker

A daily performance tracker for the Self-Made Protocol (SMP) fitness program.
Logs sleep, water intake, and step count. Predicts goal achievement using a
trained Random Forest classifier and generates a coaching message.

## What It Does

- Accepts daily check-in data (sleep hours, water glasses, steps)
- Predicts whether the 10,000-step goal will be hit
- Returns a confidence score and a direct coaching message
- Exports a weekly summary report as JSON

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```python
from tracker import analyze_day

result = analyze_day(sleep_hr=7.5, water_glasses=9, bench_kg=88)
print(result["coaching"])
```

## Sample Output

```
Prediction: HIT GOAL (88% confidence)
Coach: Strong inputs, strong output. Baseline is locked in. Keep this pattern consistent.
```

## Stack

Python, scikit-learn, pandas, FastAPI

