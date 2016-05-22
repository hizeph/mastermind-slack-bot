from controller import Controller
from slackclient import SlackClient
import time

def main ():
	controller = Controller()

	token = ""
	sc = SlackClient(token)

	if sc.rtm_connect():
		while True:
			events = []
			events = sc.rtm_read()
			if (events != []):
				print (events)
				for event in events:
					if (event.get('type', None) == 'message' and event.get('team', None) is not None):
						ans = controller.evaluateInput(event.get('text', 'None'))
						sc.rtm_send_message(event['channel'], ans)
						pass
						
			time.sleep(1)
	else:
		print ("Connection Failed, invalid token?")


if __name__ == "__main__":
	main()
