# Student Performance Analytics System

A beginner-friendly Python data-analysis project based on the EWB Courses Python with AI assignment.

## Technologies
- Python
- Pandas for loading, organizing, filtering and summarizing student records
- NumPy for numerical calculations and pass/fail status

## Features
- Reads 20 sample student records from `students.csv`
- Calculates total and average marks
- Assigns grades
- Identifies pass/fail students
- Calculates class statistics and attendance average
- Compares average marks by subject
- Lists the top five students
- Saves the analyzed data to `student_analysis_results.csv`

## Grading and pass rules
- A+: average >= 90
- A: average >= 80
- B: average >= 70
- C: average >= 60
- D: average >= 50
- F: average < 50
- Pass: at least 40 marks in every subject; otherwise Fail

These are project-defined rules. Change them if your trainer specifies different rules.

## How to run
1. Install Python 3.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   python -m pip install pandas numpy
   ```
4. Run:
   ```bash
   python main.py
   ```

## Files
- `main.py` — main program and reusable functions
- `students.csv` — sample dataset (20 records)
- `PROJECT_DOCUMENTATION.md` — project write-up template

## Before submission
Review the code and make sure you understand each function. Replace or update sample records if required, run the project, capture your own output screenshot, and add your name/college details to the documentation. Then upload the project files to your GitHub repository as instructed by your trainer.
