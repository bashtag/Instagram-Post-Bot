from window import Window
from window import isValidWindow
from constants import Const
from pyperclip import copy
from subprocess import check_output
from shutil import rmtree

constnts = Const()

num_of_users = len(constnts.USERNAMES)

while num_of_users > 0:

	if isValidWindow(num_of_users):
		first_window = Window(constnts.USERNAMES[num_of_users - 1], constnts.PASSWORDS[num_of_users - 1], constnts.PHOTO_PATHS[num_of_users - 1], "tr")

	if isValidWindow(num_of_users - 1):
		second_window = Window(constnts.USERNAMES[num_of_users - 2], constnts.PASSWORDS[num_of_users - 2], constnts.PHOTO_PATHS[num_of_users - 2], "tr")
	
	if isValidWindow(num_of_users - 2):
		third_window = Window(constnts.USERNAMES[num_of_users - 3], constnts.PASSWORDS[num_of_users - 3], constnts.PHOTO_PATHS[num_of_users -3], "tr")

	# log in
	if isValidWindow(num_of_users):
		first_window.logIn(7 if num_of_users % 3 == 1 else 0)
	if isValidWindow(num_of_users - 1):
		second_window.logIn(7 if num_of_users % 3 == 2 else 0)
	if isValidWindow(num_of_users - 2):
		third_window.logIn(7 if num_of_users % 3 == 0 else 0)

	# is log in ? else close the relative driver
	if isValidWindow(num_of_users) and first_window.getWindowFlag():
		first_window.setWindowFlag(first_window.isLogIn())
		if not first_window.getWindowFlag():
			first_window.close_driver()

	if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
		second_window.setWindowFlag(second_window.isLogIn())
		if not second_window.getWindowFlag():
			second_window.close_driver()

	if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
		third_window.setWindowFlag(third_window.isLogIn())
		if not third_window.getWindowFlag():
			third_window.close_driver()

	# if there is a save log in text, pass the removed posts part
	if isValidWindow(num_of_users) and first_window.getWindowFlag() and first_window.isThereSaveLogIn() == False:
		first_window.passRemovedPosts()
		first_window.passCockies()
		
	if isValidWindow(num_of_users - 1) and second_window.getWindowFlag() and second_window.isThereSaveLogIn() == False:
		second_window.passRemovedPosts()
		second_window.passCockies()
		
	if isValidWindow(num_of_users - 2) and third_window.getWindowFlag() and third_window.isThereSaveLogIn() == False:
		third_window.passRemovedPosts()
		third_window.passCockies()

	for hashtags in constnts.HASHTAGS:
		
		# uploading a photo with hashtags
		if isValidWindow(num_of_users) and first_window.getWindowFlag():
			first_window.clickNewPost(1)
		if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
			second_window.clickNewPost(1)
		if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
			third_window.clickNewPost(1)

		if isValidWindow(num_of_users) and first_window.getWindowFlag():
			first_window.sendPhoto(3)
		if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
			second_window.sendPhoto(3)
		if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
			third_window.sendPhoto(3)

		# to solve next button exception caused by photo size
		if isValidWindow(num_of_users) and first_window.getWindowFlag():
			while not first_window.sendPhotoNext(1, 0.3 if num_of_users % 3 == 1 else 0):
				"""
				print(f"\n{first_window.getUsername()} kullanıcısı için ileri butonu gözükmüyor."
						"\nFotoğrafa bir kere tıkla ve devam etmesi için enter'a bas."
						"-> ", end="")
				input()
				"""
				first_window.maxMinWindow()

		if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
			while not second_window.sendPhotoNext(1, 0.3 if num_of_users % 3 == 2 else 0):
				"""
				print(f"\n{second_window.getUsername()} kullanıcısı için ileri butonu gözükmüyor."
						"\nFotoğrafa bir kere tıkla ve devam etmesi için enter'a bas."
						"-> ", end="")
				input()
				"""
				second_window.maxMinWindow()

		if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
			while not third_window.sendPhotoNext(1, 0.3 if num_of_users % 3 == 0 else 0):
				"""
				print(f"\n{third_window.getUsername()} kullanıcısı için ileri butonu gözükmüyor."
						"\nFotoğrafa bir kere tıkla ve devam etmesi için enter'a bas."
						"-> ", end="")
				input()
				"""
				third_window.maxMinWindow()
			
		if isValidWindow(num_of_users) and first_window.getWindowFlag():
			first_window.sendPhotoNext(1, 0.3 if num_of_users % 3 == 1 else 0)
		if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
			second_window.sendPhotoNext(1, 0.3 if num_of_users % 3 == 2 else 0)
		if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
			third_window.sendPhotoNext(1, 0.3 if num_of_users % 3 == 0 else 0)

		copy(constnts.CAPTION)
		if isValidWindow(num_of_users) and first_window.getWindowFlag():
			first_window.pasteWithActionKeys(2)
		if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
			second_window.pasteWithActionKeys(2)
		if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
			third_window.pasteWithActionKeys(2)

		if isValidWindow(num_of_users) and first_window.getWindowFlag():
			first_window.sendHashtags(hashtags)
		if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
			second_window.sendHashtags(hashtags)
		if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
			third_window.sendHashtags(hashtags)

		if isValidWindow(num_of_users) and first_window.getWindowFlag():
			first_window.shareButton()
		if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
			second_window.shareButton()
		if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
			third_window.shareButton()

		# to solve the cannot upload posts error
		if isValidWindow(num_of_users) and first_window.getWindowFlag() and not first_window.waitForSharedText(20):
			"""
			print(f"\nResolve the error \"Cannot upload posts\" for {first_window.getUsername()} user.\n"
					"And press enter.\n"
					"Or kill this window press 1.\n-> ", end='')
			"""
			print(f"\nPost yüklenemiyor hatasını {first_window.getUsername()} kullanıcı için çöz.\n"
					"Çözdüğün vakit enter'a bas.\n"
					"Ya da pencereyi kapatmak için 1'e bas.\n-> ", end='')
			flag = input()
			if not first_window.passRemovedPosts():
				first_window.exitButton()

			if flag == "":
				first_window.resharing(hashtags)
			else:
				first_window.close_driver()
				first_window.setWindowFlag(False)
		if isValidWindow(num_of_users - 1) and second_window.getWindowFlag() and not second_window.waitForSharedText(20):
			"""
			print(f"\nResolve the error \"Cannot upload posts\" for {second_window.getUsername()} user.\n"
					"And press enter.\n"
					"Or kill this window press 1.\n-> ", end='')
			"""
			print(f"\nPost yüklenemiyor hatasını {second_window.getUsername()} kullanıcı için çöz.\n"
					"Çözdüğün vakit enter'a bas.\n"
					"Ya da pencereyi kapatmak için 1'e bas.\n-> ", end='')
			flag = input()
			if not second_window.passRemovedPosts():
				second_window.exitButton()

			second_window.exitButton()
			if flag == "":
				second_window.resharing(hashtags)
			else:
				second_window.close_driver()
				second_window.setWindowFlag(False)
		if isValidWindow(num_of_users - 2) and third_window.getWindowFlag() and not third_window.waitForSharedText(20):
			"""
			print(f"\nResolve the error \"Cannot upload posts\" for {third_window.getUsername()} user.\n"
					"And press enter.\n"
					"Or kill this window press 1.\n-> ", end='')
			"""
			print(f"\nPost yüklenemiyor hatasını {third_window.getUsername()} kullanıcı için çöz.\n"
					"Çözdüğün vakit enter'a bas.\n"
					"Ya da pencereyi kapatmak için 1'e bas.\n-> ", end='')
			flag = input()
			if not third_window.passRemovedPosts():
				third_window.exitButton()

			third_window.exitButton()
			if flag == "":
				third_window.resharing(hashtags)
			else:
				third_window.close_driver()
				third_window.setWindowFlag(False)

		if isValidWindow(num_of_users) and first_window.getWindowFlag():
			first_window.exitButton()
		if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
			second_window.exitButton()
		if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
			third_window.exitButton()

	if isValidWindow(num_of_users) and first_window.getWindowFlag():
		first_window.close_driver()
	if isValidWindow(num_of_users - 1) and second_window.getWindowFlag():
		second_window.close_driver()
	if isValidWindow(num_of_users - 2) and third_window.getWindowFlag():
		third_window.close_driver()

	num_of_users -= 3

	# To delete temporary files
	# We need to delete temporary files caused by the volume covered by selenium webdriver
	rmtree(check_output("ECHO %temp%", shell=True).decode("utf-8").strip("\r\n"), ignore_errors=True)
