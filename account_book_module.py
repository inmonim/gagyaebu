import pandas as pd
import numpy as np

df = pd.read_excel('./가계부.xlsx')
setting = pd.read_excel('./setting.xlsx')


def fix_year():
    setting = pd.read_excel('./setting.xlsx')
    year = setting.loc[0,'기본연도']
    f_year = input(f'기본 설정할 연도를 정하십시오. 현재 설정 연도 = {year} (ex> 2022)')
    if f_year.isdigit() == True:
        setting.loc[0, '기본연도'] = int(f_year)
        print(f'기본 연도가 {f_year}로 바뀌었습니당')
    else:
        print('형식에 맞춰 입력해줘용')
    setting.to_excel('./setting.xlsx', index=False)
    setting = pd.read_excel('./setting.xlsx')
    return setting.loc[0,'기본연도']


def fix_month():
    setting = pd.read_excel('./setting.xlsx')
    month = setting.loc[0,'기본월']
    f_month = input(f'기본 설정할 월을 정하십시오. 현재 설정 월 = {month} (ex> 07)')
    if f_month.isdigit() == True:
        setting.loc[0, '기본월'] = int(f_month)
        print(f'기본 월이 {f_month}로 바뀌었습니당')
    else:
        print('형식에 맞춰 입력해줘용')
    setting.to_excel('./setting.xlsx', index=False)
    setting = pd.read_excel('./setting.xlsx')
    return setting.loc[0,'기본월']




def month_input():
    while True:
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
    while True:
        day_input = input('일을 입력하십시오.: ')
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
    while True:
        in_ex_input = input('수익 / 지출')
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
    while True:
        much = input('숫자로만 입력해주세요: ')
        if much.isdigit() == True:
            return int(much)
        else:
            continue


def main_category(category):
    while True:

        main = input(f'{category} 중 선택해주시기 바랍니다. :')

        if main not in category:
            append_main = input('새로운 대분류를 추가하시겠습니까? y/n')
            if append_main in ['y', 'Y', '네', '예']:
                print('새로운 대분류가 추가되었습니다.')
                return main
            else:
                print('대분류를 다시 입력해주시기 바랍니다.')
                continue
        else:
            return main


def sub_category(category):
    while True:
        sub = input(f'{category} 중에서 선택해주시기바랍니다.')

        if sub not in category:
            append_sub = input('새로운 소분류를 추가하시겠습니까? y/n')
            if append_sub in ['y','Y','네','예']:
                print('새로운 소분류가 추가되었습니다.')
                return sub
            else:
                print('소분류를 다시 입력해주시기 바랍니다.')
                continue
        else:
            return sub


def detail():
    detail = input('세부 사항에 대해 작성해주십시오. :')
    if detail == '':
        return '없음'
    return detail


def rating():
    while True:
        rating_dict = {5: '훌륭', 4: '괜찮', 3: '애매', 2:'왜샀노', 1:'흑우', 0:'킹쩔수없음'}
        rating = int(input('소비자 평가 부탁드려요잉'))
        if rating in [0, 1,2,3,4,5]:
            return rating_dict[rating]
        else:
            print('다시 입력해주세용')


def camel_pay():
    while True:
        camelia = input('동백전으로 사용하셨나요? y/n')
        if camelia in ['y', 'Y', '네', '예','ㅇㅇ','ㅇ']:
            return 'Y'
        elif camelia in ['n','N','노','no','NO','ㄴㄴ','ㄴ']:
            return 'N'
        else:
            continue


def fixed_expenses():
    while True:
        fi_ex = input('고정 지출인가용? y/n')
        if fi_ex in ['y', 'Y', '네', '예','ㅇㅇ','ㅇ']:
            return 'Y'
        elif fi_ex in ['n','N','노','no','NO','ㄴㄴ','ㄴ']:
            return 'N'
        else:
            continue