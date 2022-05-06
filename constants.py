import os

FOLDER_NAMES = ["account-1", "account-2","account-3", "account-4","account-5", "account-6"]
USER_INFO_FILE_NAME = "userInfos.txt"
CAPTION_FILE_NAME = "caption.txt"
HASHTAGS_FILE_NAME = "hashtags.txt"

"""
	for file and constant operations
"""
class Const:

	PHOTO_NAMES: list[str] = []
	PHOTO_PATHS: list[str] = []

	USERNAMES: list[str] = []
	PASSWORDS: list[str] = []

	CAPTION: str = ""
	HASHTAGS = []

	def __init__(self) -> None:
		self.current_directory = os.getcwd()

		self.getPhotoPaths()
		self.getUserInfos()
		self.getCaption()
		self.getHashTags()

	# for photo paths
	def getPhotoPaths(self):
		flag = True

		for folder in FOLDER_NAMES:
			if flag == False:
				break

			try:
				photo_name = os.walk(rf"{self.current_directory}\\{folder}").__next__()[2][0]
				self.PHOTO_NAMES.append(photo_name)
				self.PHOTO_PATHS.append(f"{self.current_directory}\\{folder}\\{photo_name}")
			except:
				flag = False

	# to get usernames and passwords
	def getUserInfos(self):

		with open(f"{self.current_directory}\\{USER_INFO_FILE_NAME}", "r", encoding="utf8") as u_p_file:

			while True:
				user_entry = u_p_file.readline()

				if user_entry == "" or user_entry[0] in " \t\n\v\r\f":
					break
				self.USERNAMES.append(user_entry.strip("\n"))
					
				user_entry = u_p_file.readline()

				if user_entry == "" or user_entry[0] in " \t\n\v\r\f":
					break
				self.PASSWORDS.append(user_entry.strip("\n"))


	def getCaption(self):
		
		with open(f"{self.current_directory}\\{CAPTION_FILE_NAME}", "r", encoding="utf8") as caption_file:
			self.CAPTION += caption_file.read()
	

	def getHashTags(self):
		
		with open(f"{self.current_directory}\\{HASHTAGS_FILE_NAME}", "r", encoding="UTF-8") as hashtags_file:
			
			self.HASHTAGS = hashtags_file.read().split(".")