from lib2to3.pgen2.pgen import DFAState
import numpy as np
import pandas as pd
from account_book_module import *

df = pd.read_excel('./가계부.xlsx')
setting = pd.read_excel('./setting.xlsx')

while True:

    excecution = input('''===============================================================
                    Account Book
===============================================================

1. 새로운 내역 입력하기

2. 가계부 조회

3. 기본 연,월 바꾸기

4. 마지막 목록 지우기

5. 저장하고 나가기

===============================================================

실행할 행동을 선택해주세요 >>> ''')
    if excecution == '1':
        year = setting.loc[0, '기본연도']
        month = setting.loc[0, '기본월']

        day = day_input(month)
        if day == 'exit':
            continue
        in_or_ex = in_ex()
        if in_or_ex == 'exit':
            continue
        much = how_much()
        if much == 'exit':
            continue
        category = list(df.loc[:, '대분류'].unique())
        maincategory = main_category(category)
        if maincategory == 'exit':
            continue
        subcategory_list = list(df.loc[df.loc[: , '대분류']==maincategory, '소분류'].unique())
        subcategory = sub_category(subcategory_list)
        if subcategory == 'exit':
            continue
        de = detail()
        if de == 'exit':
            continue
        rate = rating()
        if rate == 'exit':
            continue
        pay = camel_pay()
        if pay == 'exit':
            continue
        fi_ex = fixed_expenses()
        if fi_ex == 'exit':
            continue

        input_data = {
            '연도' : [year], '월' : [month], '일' :[day],
            '수익/지출': [in_or_ex], '금액': [much],
            '대분류': [maincategory], '소분류': [subcategory],
            '항목명': [de], '평가': [rate], '동백전유무': [pay], '고정지출': [fi_ex]
            }

        append_df = pd.DataFrame(input_data)
        df = pd.concat([df, append_df], ignore_index=True)
        continue

    if excecution == '2':
        check_10(df)
    
    if excecution == '4':
        df = del_last(df)

    if excecution == '5':
        break
    

df.to_excel('./가계부.xlsx', index=False)
setting.to_excel('./setting.xlsx', index=False)