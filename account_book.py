import numpy as np
import pandas as pd
from account_book_module import *

df = pd.read_excel('./가계부.xlsx')
setting = pd.read_excel('./setting.xlsx')

while True:

    excecution = input('''===============================================================
    account book
    ===============================================================
    
    1. 새로운 내역 입력하기

    2. 가계부 조회

    3. 기본 연,월 바꾸기

    4. 연, 월 자유입력

    ''')

    if excecution == '1':
        year = setting.loc[0, '기본연도']
        month = setting.loc[0, '기본월']
        day = day_input(month)
        in_or_ex = in_ex()
        much = how_much()
        category = list(df.loc[:, '대분류'].unique())
        maincategory = main_category(category)
        subcategory_list = list(df.loc[df.loc[: , '대분류']==maincategory, '소분류'].unique())
        subcategory = sub_category(subcategory_list)
        de = detail()
        rate = rating()
        pay = camel_pay()
        fi_ex = fixed_expenses()

        input_data = {
        '연도' : [year], '월' : [month], '일' :[day],
        '수익/지출': [in_or_ex], '금액': [much],
        '대분류': [maincategory], '소분류': [subcategory],
        '항목명': [de], '평가': [rate], '동백전유무': [pay], '고정지출': [fi_ex]
        }

        append_df = pd.DataFrame(input_data)

        df = pd.concat([df, append_df], ignore_index=True)
        continue

    if excecution == '5':
        break
    

df.to_excel('./가계부.xlsx', index=False)
setting.to_excel('./setting.xlsx', index=False)