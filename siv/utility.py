""" The utility module for the ssystem package """
import numpy as np
from scipy import interpolate
import logging, sys,os

loglevel = logging.DEBUG

def get_basedir() :
	""" Get the base directory of the project"""
	paths = os.path.split 
	pathr = os.path.realpath
	pathd = os.path.dirname
	pathj = os.path.join
	pathe = os.path.exists
	scriptname = sys.argv[0]	
	scriptdir = pathr(pathd(scriptname))
	basedir = paths(scriptdir)[0]
	return basedir

def get_logdir() : 
	""" Get the directory of the logs folder"""
	logdir = os.path.join(basedir,'logs')	
	return logdir

basedir = get_basedir()
logdir = get_logdir()

def make_logdir() :
	""" Creates a log directory if it does not exist"""
	logdir = get_logdir()
	if not os.path.exists(logdir) : 
		os.mkdir(logdir)

def same_dict(x,y):	
	"""
	Accepts two dicts x and y ; returns if they are the same 
	"""
	n_common = len(set(x.items()) & set(y.items()) )
	return len(x)==len(y) and n_common==len(x)

class SIVLogger(object) : 
	""" Contains Loggers, Handlers and Formatters for SIV
Mostly contains static members that can be imported directly without reinitializing"""
	_handler_args = {
		'filename' : os.path.join(logdir,'siv.log') ,
		'mode' : 'a'
	}
	# Handler for writing to ssystem.log
	ssh = logging.FileHandler(**_handler_args) 
	ssh.setLevel(logging.INFO)
	
	_handler_args = {
		'filename' : os.path.join(logdir,'debug.log') ,
		'mode' : 'w'
	}
	# Handler for writing to debug.log , more detailed logs
	dh = logging.FileHandler(**_handler_args) 
	dh.setLevel(logging.DEBUG)

	ch  = logging.StreamHandler() 
	ch.setLevel(logging.WARNING)

	fmt_ch_str = "%(name)s: %(levelname)s %(message)s"
	fmt_ch = logging.Formatter(fmt_ch_str)
	ch.setFormatter(fmt_ch)

	fmt_ssh_str = "%(name)s: %(levelname)s %(message)s"
	fmt_ssh = logging.Formatter(fmt_ssh_str)
	ssh.setFormatter(fmt_ssh)
	
	fmt_dh_str = "%(name)s: %(levelname)s %(message)s"
	fmt_dh = logging.Formatter(fmt_dh_str)
	dh.setFormatter(fmt_dh)

	sivlogger = logging.getLogger("siv")	
	sivlogger.setLevel(loglevel)
	sivlogger.addHandler(ssh)
	sivlogger.addHandler(dh)
	sivlogger.addHandler(ch)
	#	sslogger.addHandler(dh)

	def __init__(self) : 
		pass


if __name__ == '__main__' : 
	make_logdir()
	logger = SIVLogger.sivlogger
	logger.info("Test")
	
	logger2 = logging.getLogger('siv.foo')
	logger2.info('Foo test')	
	logger2.debug('Foo Debug test')
	logger.warning('Serious stuff..!')

	print get_logdir()
	print get_basedir()
