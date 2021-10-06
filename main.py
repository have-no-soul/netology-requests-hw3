import datetime
from pprint import pprint
import calendar
import requests

API_URL = 'https://api.stackexchange.com/2.3/questions'
TAG = 'Python'
site = 'stackoverflow'


def get_two_last_days_questions_with_tag(tag):
	tag = TAG

	today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
	unix_t = calendar.timegm(today.utctimetuple())

	last_two_days = today - datetime.timedelta(days=2)
	unix_ltd = calendar.timegm(last_two_days.utctimetuple())

	params = {
		'fromdate': unix_ltd,
		'todate': unix_t,
		'tagged': tag,
		'site': site
	}

	url = requests.get(url=API_URL, params=params)
	pprint(url.json())


if __name__ == '__main__':
	get_two_last_days_questions_with_tag(TAG)
