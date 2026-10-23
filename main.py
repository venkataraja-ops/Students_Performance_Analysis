import pandas as pd
import numpy as np

from functions import (
    calculate_totals_and_averages, 
    assign_grade, 
    check_pass_fail, 
    get_subject_averages
)

def main():
    print("--- STUDENT PERFORMANCE ANALYTICS SYSTEM ---\n")
    
    # 1. Read the Data using Pandas
    try:
        df = pd.read_csv('students.csv')
    except FileNotFoundError:
        print("Error: 'students.csv' not found in the directory.")
        return
    
    print(f"Successfully loaded {len(df)} student records.")
    
    # 2. Process the Data (Totals, Averages, Grades, Pass/Fail)
    df = calculate_totals_and_averages(df)
    df['Grade'] = df['Average_Marks'].apply(assign_grade)
    df = check_pass_fail(df)
    
    # 3. Perform Analysis
    overall_class_avg = np.mean(df['Average_Marks'].values)
    pass_count = (df['Status'] == 'Pass').sum()
    fail_count = (df['Status'] == 'Fail').sum()
    subject_avgs = get_subject_averages(df)
    top_student = df.loc[df['Average_Marks'].idxmax()]
    
    # 4. Display Final Output clearly
    print(f"\nOverall Class Average: {overall_class_avg:.2f}")
    print(f"Students Passed: {pass_count} | Students Failed: {fail_count}")
    
    print("\nSubject-wise Averages:")
    for subj, avg in subject_avgs.items():
        print(f"  - {subj}: {avg:.2f}")
        
    print(f"\nTop Performing Student: {top_student['Name']} ({top_student['Department']}) with Average: {top_student['Average_Marks']:.2f}")

if __name__ == "__main__":
    main()