from time import sleep
import random

from selenium import webdriver
from faker import Faker
import markovify


locations = None
with open('locations.txt', 'r') as f:
	locations = f.readlines()

def randloc():
	return locations[random.randint(0, len(locations)-1)]


text_model = None
with open('corpus.txt') as f:
	text_model = markovify.Text(f.read())

def randsentence():
	s = None
	while s == None:
		s = text_model.make_sentence()
	return s


emails = ['aol.com', 'yahoo.com']
def randemaildomain():
	return emails[random.randint(0, len(emails)-1)]



fake = Faker()

browser = webdriver.Firefox()


def typerrr(b, s):
	for c in s:
		b.send_keys(c)
		sleep(random.uniform(0.02, 0.14))
	sleep(random.uniform(0.3, 0.7))


def scrollrrr():
	h = int(browser.execute_script('return document.body.scrollHeight / 6'))
	for i in range(1, h + random.randint(-10, 10), int(h/42)):
		browser.execute_script('window.scrollTo(0, ' + str(i) + ')')
		sleep(random.uniform(0.003, 0.006))


def shitontheform():
	browser.get('https://libertyallianceusa.com/woke-heat-map/')
	sleep(random.uniform(0.7, 1.2))
	scrollrrr()
	sleep(random.uniform(0.2, 0.8))
	i_fn = browser.find_element('id', 'input_83_1')
	i_ln = browser.find_element('id', 'input_83_2')
	i_em = browser.find_element('id', 'input_83_3')
	i_ph = browser.find_element('id', 'input_83_11')
	i_lo = browser.find_element('id', 'input_83_9')
	i_ds = browser.find_element('id', 'input_83_10')
	i_sm = browser.find_element('id', 'gform_submit_button_83')
	fn = fake.first_name()
	ln = fake.last_name()
	typerrr(i_fn, fn)
	typerrr(i_ln, ln)
	typerrr(i_em, fn.lower() + ln.lower() + str(random.randint(0, 99)) + "@" + randemaildomain())
	typerrr(i_ph, fake.phone_number())
	typerrr(i_lo, randloc())
	typerrr(i_ds, randsentence())
	i_sm.click()


while True:
	shitontheform()
	sleep(random.uniform(1, 3))