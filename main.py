import pandas as pd
import MySQLLink
import openaiLink
import PySimpleGUI as gui
from search_engine import SearchEngine
import openai



def main():
    #APP LAYOUT
    gui.theme('DarkGrey7')
    ttk_style = 'clam'


    layout_left = [
        [gui.Text('What question do you have?')],
        [gui.In(size = (100, 10), enable_events = True, key = 'user_question')],
        [gui.Text('Results: ')],
        [gui.Listbox(values = [], enable_events = True, size = (150, 5), key = 'Responses')],
        [gui.Text('')],
        [gui.Button('None of these questions quite match what you are looking for? Click here to auto generate a response!', key = 'GPT', size = (150, 1), use_ttk_buttons = True)],
        [gui.Text('Responses generated are not created by this company and may not be accurate.')]
        ]
    layout_right = [
        [gui.Text('')],
        [gui.Text('Output')],
        [gui.Multiline(size = (75, 5), key = 'Output')],
        [gui.Text('')],
        [gui.Button('Click here to request a question you wish to be added to our database!', key = 'Request_Database', size = (75, 1), use_ttk_buttons = True)],
        
    ]

    layout = [
        [gui.Column(layout_left), gui.Column(layout_right)]
    ]

    window = gui.Window('Chatbot', layout, ttk_theme = ttk_style)
    MySQL = MySQLLink.SQLLink()
    saved_queries = MySQL.get_data()
    engine = SearchEngine(saved_queries)
    

    while True:
        event, values = window.read()
        question = ''
        ranking_index = ''
        ranking_string = ''

        if event == 'user_question':
            window['Output'].update(None)
            question = values['user_question']
            ranking_index = engine.search(question)
            if ranking_index is None or len(ranking_index) == 0:
                
                if ' ' in question:
                    window['Responses'].update(['No responses found'])
                else:
                    window['Responses'].update('')
            else:
                ranking_string = []
                for item in ranking_index:
                    ranking_string.append(saved_queries.loc[item, 'question_column'])
                if len(ranking_string) > 10:
                    ranking_string = ranking_string[:10]
                window['Responses'].update(ranking_string)
        
        if event == 'Responses':
            if len(values['Responses']) > 0:
                if (values['Responses'][0] != '') and (values['Responses'][0] != 'No responses found'):
                    index = list(saved_queries['question_column']).index(values['Responses'][0])
                    response = saved_queries.loc[index, 'answer_column']
                    window['Output'].update(response)
                

        if event == 'GPT':
            question = values['user_question']
            window['Responses'].update(['Auto generating response...'])
            window.Refresh()
            openai.api_key = ''
            current = ''
            for chunk in openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "user",
                    "content": 'Do not mention that you are an AI model. Answer in a short response. ' + question
                }],
                stream=True,
            ):

                content = chunk["choices"][0].get("delta", {}).get("content")
                if content is not None:
                     current += content
                     window['Output'].update(current)
                     window.Refresh()
                     
            window['user_question'].update('')
            window['Responses'].update([''])
        
        if event == 'Request_Database':
            question = values['user_question']
            if question is not None and len(question) > 1:
                MySQL.add_data(question)
            window['user_question'].update('')
        
        

        if event == gui.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    main()



