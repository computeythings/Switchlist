import time

ERROR = 1
WARN = 3
INFO = 5
DEBUG = 7
LEVEL = INFO
LOGFILE = None
INIT = False

def init(outfile, level=INFO):
	global LOGFILE, INIT, LEVEL
	LEVEL = level
	LOGFILE = open(outfile, 'w')
	INIT = True
	debug('logfile initiated')

def writelog(msg, level):
	global LOGFILE, INIT, LEVEL
	
	if level <= LEVEL:
		print(msg)
		if INIT:
			try:
				LOGFILE.write(msg + '\n')
			except:
				print(msg)

def levelcode(level):
	if level == 1:
		return 'ERROR'
	if level == 3:
		return 'WARN'
	if level == 5:
		return 'INFO'
	if level == 7:
		return 'DEBUG'
	return 'LOG'
		
def error(msg, function=''):
	log(msg, function, ERROR)
def warn(msg, function=''):
	log(msg, function, WARN)
def info(msg, function=''):
	log(msg, function, INFO)
def debug(msg, function=''):
	log(msg, function, DEBUG)
def log(msg, function='', level=0):
	if level == 0:
		level = INFO
	if function != '':
		function += '()'
	now = time.time()
	writelog('%s %s:%s - %s' % (now,function,levelcode(level),msg), level)
	
def end():
	global LOGFILE, INIT
	if INIT:
		LOGFILE.close()
	
def __del__():
	global LOGFILE, INIT
	if INIT:
		LOGFILE.close()