import re
import json

text_file = open('500 G.A. Question CHSL 2019 Rahul.txt','r+')
text = text_file.read()

questions_list = text.strip().split('\n')

questions_list = list(filter(lambda a: a not in [" ","\n",""], questions_list))

def extract(each):
    try:
        oneliner = {}
        question_start = re.search(r'*',each).end()
        question_end = re.search(r'',each).start()
            
        oneliner['question'] = each[question_start:question_end].strip()
            
        answer_start = re.search(r'',each).end()
            
        oneliner['answer'] = each[answer_start:].strip().lstrip('-')
        
        return oneliner
    except:
        return {}
    

with open('500 G.A. Question CHSL 2019 Rahul.json','w+') as out:
    for each in questions_list:
        json.dump(extract(each),out,indent=4)
    out.close()
