import pandas as pd
from AB_module import *

df = pd.read_excel('./가계부.xlsx')
setting = pd.read_excel('./setting.xlsx')

# 본 파일은 test 파일입니당

while True:

    excecution = input('''===============================================================
                    Account Book
===============================================================

1. 새로운 내역 입력하기

2. 가계부 조회

3. 마지막 목록 지우기

4. 설정

5. 저장하고 나가기

===============================================================

실행할 행동을 선택해주세요 >>> ''')

    if excecution == '1':
        input_data = data_input(df, setting)
        if input_data == False:
            continue
        else:
            append_df = pd.DataFrame(input_data)
            df = pd.concat([df, append_df], ignore_index=True)
            auto_save(df, setting)
            continue

    if excecution == '2':
        print(df.iloc[-10:,:])
    
    if excecution == '3':
        df = del_last(df)
        auto_save(df, setting)

    if excecution == '4':
        setting_in(setting)

    if excecution == '5':
        break
    

df.to_excel('./가계부.xlsx', index=False)
setting.to_excel('./setting.xlsx', index=False)