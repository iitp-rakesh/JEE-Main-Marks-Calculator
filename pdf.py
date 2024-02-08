from bs4 import BeautifulSoup
from openpyxl import Workbook
from config import questionHtml
def extract_question_answers(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
        question_answers = []
        for div in soup.find_all('div', class_='question-pnl'):
            ques_type=div.find('td', align='right', string="Question Type :").find_next_sibling('td').text.strip()
            if ques_type=='SA':
                question_id_element = div.find('td', align='right', string="Question ID :")
                given_answer_element = div.find('td', align='right', string="Given Answer :")
                if question_id_element and given_answer_element:
                    question_id = question_id_element.find_next_sibling('td').text.strip()
                    given_answer = given_answer_element.find_next_sibling('td').text.strip()
                    if given_answer=='--':
                        continue
                    # print(question_id, given_answer)
                    question_answers.append((question_id, given_answer))
            if ques_type=='MCQ':
                question_id_element = div.find('td', align='right', string="Question ID :")
                option_1=div.find('td', align='right', string="Option 1 ID :")
                option_2=div.find('td', align='right', string="Option 2 ID :")
                option_3=div.find('td', align='right', string="Option 3 ID :")
                option_4=div.find('td', align='right', string="Option 4 ID :")
                option=[option_1,option_2,option_3,option_4]
                given_answer_element = div.find('td', align='right', string="Chosen Option :")
                if question_id_element and given_answer_element:
                    question_id_element = question_id_element.find_next_sibling('td').text.strip()
                    given_answer_element = given_answer_element.find_next_sibling('td').text.strip()
                    if given_answer_element=='--':
                        continue
                    optionId=option[int(given_answer_element)-1].find_next_sibling('td').text.strip()
                    # print(question_id_element, optionId)
                    question_answers.append((question_id_element, optionId))
            
    return question_answers

def write_to_excel(data, excel_file):
    wb = Workbook()
    ws = wb.active
    ws.append(['Question ID', 'Given Answer'])
    
    for question_id, given_answer in data:
        ws.append([question_id, given_answer])
    
    wb.save(excel_file)

excel_file = 'question_answers.xlsx'

question_answers = extract_question_answers(questionHtml)
write_to_excel(question_answers, excel_file)
