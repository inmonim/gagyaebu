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

4. 마지막 목록 지우기

5. 저장하고 나가기

''')
    if excecution == '1':
        year = setting.loc[0, '기본연도']
        month = setting.loc[0, '기본월']

        day = day_input()
        if day == 'exit':
            break

        in_or_ex = in_ex()
        if in_or_ex == 'exit':
            break
        much = how_much()
        if much == 'exit':
            break
        category = list(df.loc[:, '대분류'].unique())
        maincategory = main_category(category)
        if maincategory == 'exit':
            break
        subcategory_list = list(df.loc[df.loc[: , '대분류']==maincategory, '소분류'].unique())
        subcategory = sub_category(subcategory_list)
        if subcategory == 'exit':
            break
        de = detail()
        if de == 'exit':
            break
        rate = rating()
        if rate == 'exit':
            break
        pay = camel_pay()
        if pay == 'exit':
            break
        fi_ex = fixed_expenses()
        if fi_ex == 'exit':
            break

        input_data = {
            '연도' : [year], '월' : [month], '일' :[day],
            '수익/지출': [in_or_ex], '금액': [much],
            '대분류': [maincategory], '소분류': [subcategory],
            '항목명': [de], '평가': [rate], '동백전유무': [pay], '고정지출': [fi_ex]
            }
        continue
    if excecution == '4':
        del_last(df)

    if excecution == '5':
        break
    

df.to_excel('./가계부.xlsx', index=False)
setting.to_excel('./setting.xlsx', index=False)