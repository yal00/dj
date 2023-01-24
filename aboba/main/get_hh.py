import requests
from datetime import date, timedelta
from operator import itemgetter
import re

def main():

    ##======== Преобразовать дату

    def formatDate(date):
        date_new = '.'.join(reversed(date.split('T')[0].split('-')))
        time = date.split('T')[1].split('+')[0]
        return {'date': date_new, 'time': time}

    ##======== Получаем диапазон даты для поиска вакансий

    current_date = date.today() - timedelta(days=1)
    while current_date.weekday() >= 5:
        current_date = current_date - timedelta(days=1)

    data_from = current_date
    data_to = current_date

    ##======== Поиск всех вакансий

    def get_vacancies_list(name_job):
        vacancies = []
        url = 'https://api.hh.ru/vacancies'

        for i in range(0, 20):
            par = {
                'text': name_job,
                'date_from': data_from,
                'date_to': data_to,
                'area': 113,
                'per_page': 100,
                'only_with_salary': True,
                'page': i
            }
            req = requests.get(url, params=par)
            data = req.json()
            print(data_from, data_to)
            req.close()
            for vac in data['items']:
                vacancies.append(vac)
            return vacancies

    ##======== Фильтр вакансии

    def filter_vac(vac):
        vac_new = {}
        convert_v_rubli = {
            "AZN": 35.68,
            "BYR": 23.91,
            "EUR": 59.90,
            "GEL": 21.74,
            "KGS": 0.76,
            "KZT": 0.13,
            "RUR": 1,
            "UAH": 1.64,
            "USD": 60.66,
            "UZS": 0.0055,
        }

        if vac['description'] and vac['key_skills'] and vac['employer']['name'] and vac['area']['name']:
            vac_new['name'] = vac['name']
            vac_new['description'] = re.sub(re.compile('<.*?>'), '', vac['description'])

            skills = []
            for skill in vac['key_skills']:
                skills.append(skill['name'])
            vac_new['key_skills'] = ', '.join(skills)

            vac_new['employer'] = vac['employer']['name']

            salary_currency = vac['salary']['currency']
            if not vac['salary']['to']:
                salary = int(vac['salary']['from'])
            elif not vac['salary']['from']:
                salary = int(vac['salary']['to'])
            else:
                salary = int((int(vac['salary']['to']) + int(vac['salary']['from'])) / 2)
            vac_new['salary'] = int(convert_v_rubli[salary_currency] * salary)

            vac_new['area'] = vac['area']['name']
            vac_new['published_at'] = formatDate(vac['published_at'])

            return vac_new
        else:
            return {}

    ##======== Поиск по названию

    name_job = 'Разработчик игр (GameDev)'
    vacancies = get_vacancies_list(name_job)

    ##======== Сортировка по дате

    vacancies_sort = sorted(vacancies, key=itemgetter('published_at'), reverse=True)

    #========= Получение каждой вакансии в лист

    vacancies_full = []
    for vac in vacancies_sort:
        req = requests.get('https://api.hh.ru/vacancies/' + vac['id'])
        vac_one = req.json()
        req.close()
        if not filter_vac(vac_one):
            continue
        vacancies_full.append(filter_vac(vac_one))

    vacancies_full = vacancies_full[:10]
    return vacancies_full