import re
import json

text_file = open('9000-Question-Hindi.txt','r+')
text = text_file.read()

text = text.replace('\n',' ')

questions_list = text.strip().split('\uf0b7')

questions_list = list(filter(lambda a: a not in [" ","\n",""], questions_list))

def extract(each):
    try:
        oneliner = {}
        question_start = re.search(r'प्रश् न[\s]*–[\s]*',each).end()
        question_end = re.search(r'उत् तर[\s]*–[\s]*',each).start()
            
        oneliner['question'] = each[question_start:question_end].strip()
            
        answer_start = re.search(r'उत् तर',each).end()
            
        oneliner['answer'] = each[answer_start:].strip().lstrip('-')
        
        return oneliner
    except:
        return {}
    

with open('9000-Question-Hindi.json','w+') as out:
    for each in questions_list:
        json.dump(extract(each),out,indent=4)
    out.close()
