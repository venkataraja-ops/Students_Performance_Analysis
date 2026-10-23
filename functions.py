import numpy as np
import pandas as pd

def calculate_totals_and_averages(df):
    """Calculates total and average marks for each student using NumPy."""
    subject_cols = ['Math', 'Science', 'English']
    marks_matrix = df[subject_cols].values
    df['Total_Marks'] = np.sum(marks_matrix, axis=1)
    df['Average_Marks'] = np.mean(marks_matrix, axis=1)
    return df

def assign_grade(avg):
    """Assigns a letter grade based on clearly defined grading rules."""
    if avg >= 85:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 55:
        return 'C'
    elif avg >= 40:
        return 'D'
    else:
        return 'F'

def check_pass_fail(df, passing_marks=40):
    """Determines pass or fail status based on marks and attendance conditions."""
    subject_cols = ['Math', 'Science', 'English']
    def status(row):
        if row[subject_cols].min() >= passing_marks and row['Attendance'] >= 75:
            return 'Pass'
        else:
            return 'Fail'
    df['Status'] = df.apply(status, axis=1)
    return df

def get_subject_averages(df):
    """Calculates subject-wise performance averages using NumPy."""
    subject_cols = ['Math', 'Science', 'English']
    return {col: np.mean(df[col].values) for col in subject_cols}