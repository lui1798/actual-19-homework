import os

from utils.file import ReadConfigFile





def main():
	BASEDIR = os.path.dirname(os.path.abspath(__file__))
	print(BASEDIR)
	ReadConfigFile(BASEDIR, '')




if __name__ == '__main__':
	main()