# -*- coding:utf-8 -*-
from enum import Enum
from time import sleep

from selenium import webdriver
import selenium.webdriver.support.ui as ui
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def get_song_rank_list(url, songs_time):
	print("\n-------------Start---------------")
	driver = webdriver.Chrome(
		executable_path='./drv/chromedriver')
	# https://sites.google.com/a/chromium.org/chromedriver/downloads chrome对应版本driver

	driver.get(url)
	driver.switch_to.frame('g_iframe')
	wait = ui.WebDriverWait(driver, 15)
	data = ""
	song_dict = {}

	if wait.until(lambda driver: driver.find_element_by_class_name('g-bd')):
		if songs_time == 1:
			driver.find_element_by_id('rHeader').find_element_by_id('songsall').click()
			sleep(3)

		data += driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text
		print(data)
		lists = driver.find_element_by_class_name('m-record').find_elements_by_tag_name('li')
		print("Top{}:".format(len(lists)))
		for l in lists:
			name = (l.find_element_by_tag_name('b').text).decode("utf-8")
			singer = (l.find_element_by_class_name('s-fc8').text.replace('-', '')).decode("utf-8")
			times = l.find_element_by_class_name('bg').get_attribute('style')
			song = "{}, {}, {}".format(name, singer, times)
			print(song)
			song_dict[name] = song
	return song_dict


def compare_song(dict1, dict2):
	print("\n--------------------------------")
	print("\n---->Same song between us")
	for name, song in dict1.iteritems():
		if name in dict2:
			print(song)
	print("---->End")
	print("\n--------------------------------")

SONGS_WEEK = 0
SONGS_ALL = 1
if __name__ == '__main__':
	girl = get_song_rank_list("https://music.163.com/#/user/songs/rank?id=322324034", SONGS_ALL)     # hh
	boy = get_song_rank_list("https://music.163.com/#/user/songs/rank?id=39661960", SONGS_ALL)       # zz
	compare_song(girl, boy)
