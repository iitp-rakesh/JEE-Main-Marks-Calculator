from bs4 import BeautifulSoup
from openpyxl import Workbook
from config import keyPath
def extract_question_answers(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        question_answers = []
        for tr in soup.find_all('tr', class_='form-options-item'):
            td_elements = tr.find_all('td', class_='vcenter')
            if len(td_elements) >= 2:
                question_id = td_elements[0].text.strip()
                answer = td_elements[1].text.strip()
                question_answers.append((question_id, answer))
            
    return question_answers

def write_to_excel(data, excel_file):
    wb = Workbook()
    ws = wb.active
    ws.append(['Question ID', 'Answer'])
    
    for question_id, answer in data:
        ws.append([question_id, answer])
    
    wb.save(excel_file)

excel_file = 'question_nswers.xlsx'

question_answers = extract_question_answers(keyPath)
write_to_excel(question_answers, excel_file)
