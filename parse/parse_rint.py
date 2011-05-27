import re

##Find any character that is preceded by two pipes and white space and this is followed by a colon
##This will get our grouping factor
#m = re.search(r'(?<=\|\|\s)(.+)(?=:)', 'xtmixed y x || int:, cov(un) var')
#m.group()


def grfactor(code):
	"""docstring for grfactor"""
	parse = {}
	ivdv = re.search(r'(?<=xtmixed\s)(.+)(?=\s\|\|)',code)
	ivdv = ivdv.group()
	ivdv = ivdv.rsplit()
	dv = ivdv[0]
	parse['dv'] = dv
	iv = ivdv[1:]
	parse['iv'] = iv
	subject2 = re.search(r'(?<=\|\|\s)[\w]*(?=:)', code)
	subject2 = subject2.group()
	parse['level-2-sub']=subject2
	return parse


