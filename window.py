from asyncio.windows_events import NULL
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

os.environ['PATH'] += r"C:/SeleniumDrivers"

"""
	Window class to open another pages
	Waiting seconds depend on you. Because you don't wanna wait for another pages
	Language sensitive
"""
class Window:
	def __init__(self, username, password, photo_path, lang: str = "en"):
		self.photo_path = photo_path
		self.username = username
		self.password = password
		self.window_flag = True
		self.driver = webdriver.Edge("C:\\SeleniumDrivers\\msedgedriver.exe")
		self.driver.get("https://www.instagram.com/")
		self.driver.implicitly_wait(10)

		if lang == "en":
			self.init_language()
		elif lang == "tr":
			self.init_language(new_post_label="Yeni Gönderi",
								next="İleri",
								caption_area_label="Açıklama yaz...",
								share="Paylaş",
								close="Kapat",
								login_info="Giriş Bilgilerin Kaydedilsin mi?",
								ok="Tamam",
								post_shared="Gönderin paylaşıldı.",
								may_be_del_account="Hesabın Silinebilir",
								removed_warning="Gönderin Topluluk Kurallarımıza Aykırı")

	# initialize language
	def init_language(self, login_info: str = "Save Your Login Info?",
	cockies_warning: str = "Allow the use of cookies by Instagram?",
	pass_cockies_button: str = "Only allow essential cookies",
	removed_warning: str = "Your Post Goes Against Our Community Guidelines",
	next: str = "Next",
	may_be_del_account: str = "Your Account May Be Deleted",
	ok: str = "OK",
	new_post_label: str = "New Post",
	caption_area_label: str = "Write a caption...",
	share: str = "Share",
	post_shared: str = "Your post has been shared.",
	close: str = "Close"):
		
		self.login_info = login_info
		self.cockies_warning = cockies_warning
		self.pass_cockies_button = pass_cockies_button
		self.removed_warning = removed_warning
		self.next = next
		self.may_be_del_account = may_be_del_account
		self.ok = ok
		self.new_post_label = new_post_label
		self.caption_area_label = caption_area_label
		self.share = share
		self.post_shared = post_shared
		self.close = close

	# to change photo_path for other photos (loop)
	def set_photo_path(self, new_path: str):
		self.photo_path = new_path

	# with user inputs.
	def logIn(self, seconds: int = 0):
		username_input = self.driver.find_element_by_css_selector("input[name='username']")
		password_input = self.driver.find_element_by_css_selector("input[name='password']")

		username_input.send_keys(self.username)
		password_input.send_keys(self.password + "\n")

		sleep(seconds)

	def isLogIn(self) -> bool:
		try:
			self.driver.find_element_by_css_selector("input[name='username']")
			return False
		except:
			return True

	# if there is not any removed posts text then you are able to pass the part of passing removed posts.
	def isThereSaveLogIn(self) -> bool:
		self.passCockies()
		try:
			self.driver.find_element_by_xpath(f"//div[text()='{self.login_info}']")
			return True
		except:
			return False

	def	passRemovedPosts(self, seconds: int = 5) -> bool:
		first_text = NULL
		try:
			first_text = self.driver.find_element_by_xpath(f"//h2[text()='{self.removed_warning}']")
		except:
			pass

		if first_text != NULL:
			try:
				first_button = self.driver.find_element_by_xpath(f"//button[text()='{self.next}']")
				first_button.click()
			except:
				first_button = self.driver.find_element_by_xpath(f"//button[text()='{self.ok}']")
				first_button.click()
				return None

			sleep(seconds)

			second_text = NULL
			try:
				second_text = self.driver.find_element_by_xpath(f"//h2[text()='{self.may_be_del_account}']")
			except:
				pass

			if second_text != NULL:
				second_button = self.driver.find_element_by_xpath(f"//button[text()='{self.ok}']")
				second_button.click()
			return True
		return False

	# passing cockies label
	def passCockies(self):
		try:
			self.driver.implicitly_wait(2)
			self.driver.find_element_by_xpath(f"//h2[text()='{self.cockies_warning}']")
			cockies_button = self.driver.find_element_by_xpath(f"//button[text()='{self.pass_cockies_button}']")
			cockies_button.click()
		except:
			pass

	# new post button
	def clickNewPost(self, seconds: int = 0):
		self.driver.implicitly_wait(seconds)
		
		new_post_button = self.driver.find_element_by_css_selector(f"svg[aria-label='{self.new_post_label}']")
		new_post_button.click()


	# photo chosing
	def sendPhoto(self, seconds: int = 0):
		self.driver.implicitly_wait(seconds)
		
		file_input = self.driver.find_element_by_xpath("//input[@type='file']")
		file_input.send_keys(self.photo_path)

	# next button click
	def sendPhotoNext(self, seconds: int = 0, sleep_seconds: int = 0) -> bool:
		self.driver.implicitly_wait(seconds)
		try:
			photo_next = self.driver.find_element_by_xpath(f"//button[text()='{self.next}']")
			photo_next.click()
			sleep(sleep_seconds)
			return True
		except:
			return False

	def maxMinWindow(self):
		self.driver.maximize_window()
		self.driver.minimize_window()

	# CTRL + V
	def pasteWithActionKeys(self, seconds: int = 0):
		self.driver.implicitly_wait(seconds)

		self.caption_area = self.driver.find_element_by_css_selector(f"textarea[aria-label='{self.caption_area_label}']")
		self.caption_area.send_keys("")

		ActionChains(self.driver).key_down(Keys.LEFT_CONTROL).perform()
		ActionChains(self.driver).send_keys("v").perform()
		ActionChains(self.driver).key_up(Keys.LEFT_CONTROL).perform()

	# in the list
	def sendHashtags(self, hashTags: str):
		self.caption_area.send_keys(hashTags)

	def shareButton(self):
		share_button = self.driver.find_element_by_xpath(f"//button[text()='{self.share}']")
		share_button.click()

	# waiting to complete the sharing
	"""
		It'll be return true if post can be shared, otherwise it'll be return false.
	"""
	def waitForSharedText(self, seconds: int = 0) -> bool:
		try:
			self.driver.implicitly_wait(seconds)
			self.driver.find_element_by_xpath(f"//h2[text()='{self.post_shared}']")
			return True
		except:
			return False

	def exitButton(self):
		try:
			exit_button = self.driver.find_element_by_css_selector(f"svg[aria-label='{self.close}']")
			sleep(0.02)
			exit_button.click()
		except:
			pass

	# to close webdriver
	def close_driver(self):
		self.driver.close()

	# if the post hasn't been shared.
	def resharing(self, hashtag: str):
		self.clickNewPost(1)
		self.sendPhoto(3)
		self.sendPhotoNext(1)
		self.sendPhotoNext(1)

		# maybe a bug will appear
		self.pasteWithActionKeys(2)
		self.sendHashtags(hashtag)
		self.shareButton()
		if not self.waitForSharedText(20):
			self.exitButton()
			self.resharing(hashtag)

	# username getter
	def getUsername(self) -> str:
		return self.username

	# flag setter
	def setWindowFlag(self, flag: bool):
		self.window_flag = flag

	# flag getter
	def getWindowFlag(self) -> bool:
		return self.window_flag

# is Window Valid for photo sharing
def isValidWindow(which_account: int) -> bool:

	# if there isn't any photo on related folders
	if 1 <= which_account <= 6:
		return True
	
	return False