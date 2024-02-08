import key
import pdf
import check
import os
import config
# execute the key.py file
keyhtml=key.extract_question_answers(config.keyPath)
key_file = 'question_nswers.xlsx'
key.write_to_excel(keyhtml, key_file)
# execute the pdf.py file
queshtml=pdf.extract_question_answers(config.questionHtml)
pdf_file = 'question_answers.xlsx'
pdf.write_to_excel(queshtml, pdf_file)
# execute the check file
check.check()