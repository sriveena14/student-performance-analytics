"""
Student Performance Analytics System
Technologies: Python, NumPy, Pandas

Run:
    pip install pandas numpy
    python main.py
"""
from pathlib import Path
import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).parent / "students.csv"
SUBJECTS = ["Python_Marks", "Maths_Marks", "Science_Marks"]

def load_data(file_path=DATA_FILE):
    """Load student records from a CSV file and validate required columns."""
    df = pd.read_csv(file_path)
    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance_Percent"]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing these columns: {', '.join(missing)}")
    if df.empty:
        raise ValueError("The dataset contains no student records.")
    return df

def assign_grade(average):
    """Assign a grade using the project's grading rules."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"

def add_performance_columns(df):
    """Calculate total, average, grade and pass/fail for every student."""
    result = df.copy()
    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = result[SUBJECTS].mean(axis=1).round(2)
    result["Grade"] = result["Average_Marks"].apply(assign_grade)
    # A student passes only when they score at least 40 in every subject.
    result["Result"] = np.where((result[SUBJECTS] >= 40).all(axis=1), "Pass", "Fail")
    return result

def show_student_summary(df):
    print("\n=== STUDENT PERFORMANCE SUMMARY ===")
    print(df[["Student_ID", "Name", "Department", "Total_Marks",
              "Average_Marks", "Grade", "Result", "Attendance_Percent"]]
          .to_string(index=False))

def show_class_statistics(df):
    all_marks = df[SUBJECTS].to_numpy()
    print("\n=== CLASS STATISTICS ===")
    print(f"Number of students       : {len(df)}")
    print(f"Overall class average    : {all_marks.mean():.2f}")
    print(f"Highest individual mark  : {all_marks.max()}")
    print(f"Lowest individual mark   : {all_marks.min()}")
    print(f"Students passed          : {(df['Result'] == 'Pass').sum()}")
    print(f"Students failed          : {(df['Result'] == 'Fail').sum()}")
    print(f"Pass percentage          : {(df['Result'] == 'Pass').mean() * 100:.2f}%")
    print(f"Average attendance       : {df['Attendance_Percent'].mean():.2f}%")

def show_subject_analysis(df):
    print("\n=== SUBJECT-WISE PERFORMANCE ===")
    averages = df[SUBJECTS].mean().sort_values(ascending=False)
    for subject, average in averages.items():  # Loop through each subject
        print(f"{subject.replace('_Marks', ''):15s} average: {average:.2f}")
    print(f"Best-performing subject  : {averages.index[0].replace('_Marks', '')}")
    print(f"Lowest-performing subject: {averages.index[-1].replace('_Marks', '')}")

def show_top_performers(df, count=5):
    print(f"\n=== TOP {count} STUDENTS ===")
    top = df.sort_values("Average_Marks", ascending=False).head(count)
    print(top[["Name", "Department", "Average_Marks", "Grade"]].to_string(index=False))

def save_results(df):
    output_file = Path(__file__).parent / "student_analysis_results.csv"
    df.to_csv(output_file, index=False)
    print(f"\nDetailed results saved to: {output_file.name}")

def main():
    try:
        raw_df = load_data()
        analyzed_df = add_performance_columns(raw_df)
        show_student_summary(analyzed_df)
        show_class_statistics(analyzed_df)
        show_subject_analysis(analyzed_df)
        show_top_performers(analyzed_df)
        save_results(analyzed_df)
    except FileNotFoundError:
        print("Could not find students.csv. Keep it in the same folder as main.py.")
    except (ValueError, pd.errors.ParserError) as error:
        print(f"Could not process the dataset: {error}")

if __name__ == "__main__":
    main()
