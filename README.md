# Air Quality Index (AQI) Data Cleaning & Analysis Pipeline

This is a Python-based data project that takes a raw, messy government dataset of air quality metrics across India, cleans up common sensor and formatting errors, and extracts key pollution insights.

## Project Workflow

The script is broken down into three simple phases:

1. **Phase 1: Ingestion & Diagnostics** — Loading the data and analyzing its initial shape and data types.
2. **Phase 2: Cleaning & Fixing** — Repairing broken dates, handling system glitches, clearing out missing rows, and trimming text.
3. **Phase 3: Analysis (EDA)** — Querying the clean data to find real-world insights like the most polluted states and extreme spikes.

---

## What This Pipeline Fixes

Instead of just running calculations on raw data, this script fixes several hidden issues that would otherwise mess up our analysis:

* **Fixing String Dates:** Converts the `last_update` column from flat text strings into actual Python datetime objects so we can use them for time-based analysis later.
* **Catching Fake Zeros:** Found 20 rows where the sensor read an absolute `0` for average pollution. Since a true outdoor AQI of 0 is basically impossible, these are treated as system errors, converted to `NaN`, and safely dropped.
* **Dropping Missing Data Safely:** Dropped the rows where core pollution metrics were completely missing. We intentionally chose to **drop** instead of fill (impute) because inventing numbers for health/environmental data creates fake trends.
* **Automated Whitespace Stripping:** Automatically trims hidden leading and trailing spaces from text columns like `station` and `city` to prevent grouping errors and silent failures.

---

## Tech Stack
* **Language:** Python 3
* **Libraries:** Pandas, NumPy
* **Editor:** VS Code (Built completely manually with AI autocomplete disabled to ensure code mastery!)

---

## How to Run the Script

1. Make sure you have pandas and numpy installed:
   ```bash
   pip install pandas numpy