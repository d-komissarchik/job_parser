import os
import sys

from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()


from scraping.parsers import *

from scraping.models import Vacancy, City, Language

parsers = (
    (work, 'https://www.work.ua/jobs-kyiv-python/'),
    (dou, 'https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D1%97%D0%B2&category=Python'),
    (djinni, 'https://djinni.co/jobs/?all-keywords=&any-of-keywords=&exclude-keywords=&primary_keyword=Python&region=UKR&location=kyiv'),
)
city = City.objects.filter(slug='kyiv').first()
language = Language.objects.filter(slug='python').first()

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass


# h = codecs.open('work.txt', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()
