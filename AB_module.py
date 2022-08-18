import pandas as pd

def fix_year(setting):
    for q in range(4):
        if q == 3:
            print('입력횟수를 초과하셨어양')
            return 'exit'
        year = setting.loc[0, '기본연도']
        f_year = input(f'기본 설정할 연도를 정하십시오. 현재 설정 연도 = {year} >>> ')
        if f_year.isdigit() == True:
            setting.loc[0, '기본연도'] = int(f_year)
            print(f'기본 연도가 {f_year}로 바뀌었습니당')
        else:
            print('형식에 맞춰 입력해줘용')
        setting.to_excel('./setting.xlsx', index=False)
        break


def fix_month(setting):
    for q in range(4):
        if q == 3:
            print('입력횟수를 초과하셨어양')
            return 'exit'
        month = setting.loc[0, '기본월']
        f_month = input(f'기본 설정할 월을 정하십시오. 현재 설정 월 = {month} >>> ')
        if f_month.isdigit() == True:
            setting.loc[0, '기본월'] = int(f_month)
            print(f'기본 월이 {f_month}로 바뀌었습니당')
        else:
            print('형식에 맞춰 입력해줘용')
        setting.to_excel('./setting.xlsx', index=False)
        break


def month_input():
    for q in range(4):
        if q == 3:
            print('입력횟수를 초과하셨어양')
            return 'exit'
        month_input = input('월을 입력하십시오.: ')
        month_list = []
        for i in month_input:
            if i.isdigit() == True:
                month_list.append(i)
        if len(month_list) >2 or len(month_list) == 0:
            print('형식이 맞지 않습니다. 다시 입력해주세요.')
            continue

        month_int = int(''.join(month_list))

        if month_int > 12 or month_int < 1:
            print('1월과 12월 사이로 입력해주십시오.')
            continue
        
        return month_int


def day_input(month):
    for q in range(4):
        if q == 3:
            print('입력회수 초과! 처음으로 돌아갑니당')
            return 'exit'

        day_input = input('일을 입력해주세용 >>> ')
        day_list = []

        for i in day_input:
            if i.isdigit() == True:
                day_list.append(i)
        if len(day_list) >2 or len(day_list) == 0:
            print('형식이 맞지 않습니다. 다시 입력해주세요.')
            continue

        day_int = int(''.join(day_list))

        if month == 2:
            if day_int <1 or day_int >29:
                print(f'{month}월은 1일부터 29일 사이로 입력해주십시오.')
                continue
        elif month in [1,3,5,7,8,10,12]:
            if day_int <1 or day_int >32:
                print(f'{month}월은 31일까지 있습니다.')
                continue
        else:
            if day_int <1 or day_int >31:
                print(f'{month}월은 30일까지 있습니다.')
                continue
        return day_int


def in_ex():
    for q in range(4):
        if q == 3:
            print('입력회수 초과로 처음으로 돌아갑니다.')
            return 'exit'

        in_ex_input = input('수익 / 지출  >>> ')
        if in_ex_input in ['수익','수입','이득']:
            return '수익'
        elif in_ex_input in ['지출','소비','손해']:
            return '지출'
        for i in in_ex_input:
            if i in ['수','ㅅ', 'ㅇ','익','입','이','득']:
                return '수익'
            elif i in ['지', 'ㅈ','ㅊ','지','씀','출','손','소']:
                return '지출'
        else:
            print('가능하면 알아들을 수 있게 써 주십시오.')


def how_much():
    for q in range(4):
        
        if q == 3:
            print('입력회수 초과로 처음으로 돌아갑니다.')
            return 'exit'

        much = input('금액 입력 (숫자로만 입력해주세요)  >>> ')
        if much.isdigit() == True:
            return int(much)
        else:
            print('다시 입력해주세용')


def main_category(category):
    for q in range(4):
        if q == 3:
            print('입력회수 초과로 처음으로 돌아갑니다.')
            return 'exit'

        main = input(f'{category} \n 중 선택해주시기 바랍니다.  >>> ')
        
        if main not in category:
            append_main = input('새로운 대분류를 추가하시겠습니까? y/n >>> ')
            if append_main in ['y', 'Y', '네', '예']:
                print('새로운 대분류가 추가되었습니다.')
                return main
            else:
                print('대분류를 다시 입력해주시기 바랍니다.')
                continue
        else:
            return main


def sub_category(sub_cat):
    for q in range(4):
        if q == 3:
            print('입력회수 초과로 처음으로 돌아갑니다.')
            return 'exit'

        if len(sub_cat) == 0:
            sub = input('새로운 소분류도 추가해주십시오. >>> ')
            return sub
        else:
            sub = input(f'{sub_cat} \n 중에서 선택해주시기바랍니다. >>> ')

        if sub not in sub_cat:
            append_sub = input('새로운 소분류를 추가하시겠습니까? y/n >>> ')
            if append_sub in ['y','Y','네','예','ㅇ','ㅇㅇ','ㄱ','ㄱㄱ']:
                print('새로운 소분류가 추가되었습니다.')
                return sub
            else:
                print('소분류를 다시 입력해주시기 바랍니다.')
                continue
        else:
            return sub


def detail():
    detail = input('세부 사항에 대해 작성해주십시오. >>> ')
    if detail == '':
        return '없음'
    return detail


def rating():
    for q in range(4):
        if q == 3:
            print('입력회수 초과로 처음으로 돌아갑니다.')
            return 'exit'

        rating_dict = {'5': '훌륭', '4': '괜찮', '3': '애매', '2':'왜샀노', '1':'흑우', '0':'킹쩔수없음'}

        rating = input('소비자 평가 부탁드려요잉(0 ~ 5) >>> ')
        if rating in ['0','1','2','3','4','5']:
            return rating_dict[rating]

        else:
            print('다시 입력해주세용')


def camel_pay():
    for q in range(4):
        if q == 3:
            print('입력회수 초과로 처음으로 돌아갑니다.')
            return 'exit'

        camelia = input('동백전으로 사용하셨나요? y/n')
        if camelia in ['y', 'Y', '네', '예','ㅇㅇ','ㅇ']:
            return 'Y'
        elif camelia in ['n','N','노','no','NO','ㄴㄴ','ㄴ']:
            return 'N'
        else:
            print('다시 입력해주세용')


def fixed_expenses(setting, main, sub):
    if setting.loc[0,'고정항목 자동선택'] == 'on':
        if 'M.'+main in list(setting.loc[:,'고정항목 분류']) or 'S.'+sub in list(setting.loc[:,'고정항목 분류']):
            print('고정항목으로 자동 선택 되었습니다.')
            return 'Y'

    for q in range(4):
        if q == 3:
            print('입력회수 초과로 처음으로 돌아갑니다.')
            return 'exit'

        fi_ex = input('고정 지출/수익 인가용? y/n >>> ')
        if fi_ex in ['y', 'Y', '네', '예','ㅇㅇ','ㅇ']:
            return 'Y'
        elif fi_ex in ['n','N','노','no','NO','ㄴㄴ','ㄴ']:
            return 'N'
        else:
            print('다시 입력해주세용')


def fixed_expenses_on_off(setting):
    for q in range(4):
        if q==3:
            print('입력횟수 초과했습니당')
            return 'exit'

        now_set = setting.loc[0,'고정항목 자동선택']
        print(f'현재 고정항목 자동 선택 설정: {now_set}')

        new_set = input('고정항목을 자동으로 선택하시겠습니까? y/n >>>')

        if new_set in ['on','On','ON','oN','ㅇㅇ','ㅇ','예','네','y','yes','Y','Yes']:
            setting.loc[0, '고정항목 자동선택'] = 'on'
            print('고정항목 자동저장이 on로 바뀌었습니당')
            break
        elif new_set in ['off','Off','OFF','ㄴㄴ','ㄴ','아니오','아니','ss','s']:
            setting.loc[0, '고정항목 자동선택'] = 'off'
            print('고정항목 자동저장이 off로 바뀌었습니당')
            break
        else:
            print('형식을 맞춰주세염')


def fixed_expenses_setting(df, setting):
    for q in range(4):
        if q==3:
            print('입력횟수 초과했습니당')
            return 'exit'
        
        category = list(setting.loc[:,'고정항목 분류'].unique())
        print(f'현재 고정항목 자동선택 분류: {category}')
        ex = input('무엇을 바꾸시겠습니까? 대/소 >>> ')

        if ex == '대':
            ex2 = input('삭제/추가 >>> ')
            if ex2 == '삭제':
                main = list(df.loc[:,'대분류'].unique())
                del_main = input(f'{main}\n삭제하실 대분류를 분류명만 기입해주세요 >>> ')
                if 'M.'+del_main in list(setting.loc[:,'고정항목 분류']):
                    setting.drop(setting[setting.loc[:,'고정항목 분류'] == 'M.'+del_main].index, inplace=True)
                    print('대분류가 삭제되었습니다.')
                else:
                    print('다시 입력해주세요.')
                    continue
            elif ex2 == '추가':

                insert_main = input('추가하실 대분류를 기입해주세요 >>> ')
                if insert_main in list(df.loc[:,'대분류']):
                    data = {'고정항목 분류' : ['M.'+insert_main]}
                    append_df = pd.DataFrame(data)
                    setting = pd.concat([setting, append_df], ignore_index=True)
                    print('수정되었습니당')
                else:
                    print('다시 입력해주세요.')
                    continue

        elif ex == '소':
            ex2 = input('삭제/추가 >>> ')

            if ex2 == '삭제':
                del_sub = input('삭제하실 소분류를 기입해주세요 >>> ')
                if 'S.'+del_sub in list(setting.loc[:,'고정항목 분류']):
                    setting.drop(setting[setting.loc[:,'고정항목 분류'] == 'S.'+del_sub].index,inplace=True)
                    print('소분류가 삭제되었습니다.')
                else:
                    print('다시 입력해주세요.')
                    continue

            elif ex2 == '추가':
                sub = list(df.loc[:,'소분류'].unique())
                insert_sub = input(f'{sub}\n추가하실 소분류를 기입해주세요 >>> ')
                if insert_sub in list(df.loc[:,'소분류']):
                    data = {'고정항목 분류' : ['S.'+insert_sub]}
                    append_df = pd.DataFrame(data)
                    setting = pd.concat([setting, append_df], ignore_index=True)
                    print('수정되었습니당')
                else:
                    print('다시 입력해주세요.')
                    continue
        setting.to_excel('./setting.xlsx', index=False)
        return setting


def del_last(df):
    for q in range(4):
        if q == 3:
            print('입력회수 초과로 처음으로 돌아갑니다.')
            return 'exit'
        
        last_contents = f'''현재 마지막 항목
=============================================
{df.iloc[-1,:]}
=============================================
'''
        print(last_contents)
        del_last = input('마지막 항목을 지우시겠습니까?(y/n): ')
        if del_last in ['y','Y', '예','ㅇ','ㄱㄱ','ㄱ','o','O','네']:
            print(last_contents)
            return df.iloc[:-1, :]
        elif del_last in ['n','N','ㄴ','아니','아니요','ㄴㄴ','s','no','NO']:
            print(last_contents)
            return df
        else:
            print('다시 입력해주세양')
            print(last_contents)


def data_input(df, setting):
    year = setting.loc[0, '기본연도']
    month = setting.loc[0, '기본월']

    day = day_input(month)
    if day == 'exit':
        return False
    in_or_ex = in_ex()
    if in_or_ex == 'exit':
        return False
    elif in_or_ex == '지출':
        much = how_much()
        if much == 'exit':
            return False
        category = list(df.loc[df.loc[:,'수익/지출'] == '지출', '대분류'].unique())
        maincategory = main_category(category)
        if maincategory == 'exit':
            return False
        subcategory_list = list(df.loc[df.loc[: , '대분류']==maincategory, '소분류'].unique())
        subcategory = sub_category(subcategory_list)
        if subcategory == 'exit':
            return False
        de = detail()
        if de == 'exit':
            return False
        rate = rating()
        if rate == 'exit':
            return False
        pay = camel_pay()
        if pay == 'exit':
            return False
        fi_ex = fixed_expenses(setting, maincategory, subcategory)
        if fi_ex == 'exit':
            return False

        input_data = {
            '연도' : [year], '월' : [month], '일' :[day],
            '수익/지출': [in_or_ex], '금액': [much],
            '대분류': [maincategory], '소분류': [subcategory],
            '항목명': [de], '평가': [rate], '동백전유무': [pay], '고정항목': [fi_ex]
            }

        return input_data

    elif in_or_ex == '수익':
        much = how_much()
        if much == 'exit':
            return False
        category = list(df.loc[list(df.loc[:,'수익/지출'] == '수익'), '대분류'].unique())
        maincategory = main_category(category)
        if maincategory == 'exit':
            return False
        subcategory_list = list(df.loc[df.loc[: , '대분류']==maincategory, '소분류'].unique())
        subcategory = sub_category(subcategory_list)
        if subcategory == 'exit':
            return False
        de = detail()
        if de == 'exit':
            return False
        rate = None
        pay = None
        fi_ex = fixed_expenses(setting, maincategory, subcategory)
        if fi_ex == 'exit':
            return False

        input_data = {
            '연도' : [year], '월' : [month], '일' :[day],
            '수익/지출': [in_or_ex], '금액': [much],
            '대분류': [maincategory], '소분류': [subcategory],
            '항목명': [de], '평가': [rate], '동백전유무': [pay], '고정항목': [fi_ex]
            }

        return input_data


def auto_save_set(setting):
    for q in range(4):
        if q==3:
            print('입력횟수 초과했습니당')
            return 'exit'
            
        now_set = setting['자동저장'][0]
        print(f'현재 설정 : {now_set}')
        
        new_set = input('설정을 바꾸시겠습니까? on/off >>> ')
        if new_set in ['on','On','ON','oN','ㅇㅇ','ㅇ','예','네','y','yes','Y','Yes']:
            setting.loc[0, '자동저장'] = 'on'
            print('자동저장이 on로 바뀌었습니당')
        elif new_set in ['off','Off','OFF','ㄴㄴ','ㄴ','아니오','아니','ss','s']:
            setting.loc[0, '자동저장'] = 'off'
            print('자동저장이 off로 바뀌었습니당')
        else:
            print('형식을 맞춰주세염')
            continue
        setting.to_excel('./setting.xlsx', index=False)
        break


def auto_save(df, setting):
    if setting.loc[0,'자동저장'] == 'on':
        df.to_excel('가계부.xlsx', index=False)
        print('저장되었습니다.')


def setting_in(df, setting):
    while True:
            
        s = input('''
변경할 설정을 입력해주세요.

1. 기본 연도 변경

2. 기본 월 변경

3. 자동저장 on/off

4. 고정지출 자동저장 설정

5. 메인메뉴로 돌아가기

>>> ''')
        if s == '1':
            fix_year(setting)
        elif s == '2':
            fix_month(setting)
        elif s == '3':
            auto_save_set(setting)
        elif s == '4':
            s2 = input('고정항목 자동선택 on/off: 1 \n고정항목 자동선택 항목 설정: 2\n >>> ')
            if s2 == '1':
                fixed_expenses_on_off(setting)
            elif s2 == '2':
                setting = fixed_expenses_setting(df, setting)
        elif s == '5':
            return setting
        else:
            print('숫자만 입력해주세양')