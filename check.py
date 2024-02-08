import pandas as pd
def check():
    # Read the correct answers and given answers Excel files
    correct_answers_df = pd.read_excel('question_nswers.xlsx')
    given_answers_df = pd.read_excel('question_answers.xlsx')

    # Merge the two dataframes on 'Question ID'
    merged_df = pd.merge(correct_answers_df, given_answers_df, on='Question ID', how='inner')

    # Calculate marks
    merged_df['Marks'] = 0
    merged_df.loc[merged_df['Answer'] == merged_df['Given Answer'], 'Marks'] = 4  # +4 for correct match
    merged_df.loc[merged_df['Answer'] != merged_df['Given Answer'], 'Marks'] = -1  # -1 for not match

    # Sum up the marks to get total marks
    total_marks = merged_df['Marks'].sum()

    # Display the result
    print("Total Marks:", total_marks)
