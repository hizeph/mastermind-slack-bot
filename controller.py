from apiCalls import ApiCalls
import re

class Controller:

	def __init__ (self):
		self.game_api = ApiCalls()
		self.game_key = None
		self.guessHistory = None
		
	def evaluateInput (self, inputMessage):
		value = re.findall('^start\s([a-zA-Z\s]{1,20}$)', inputMessage)
		if (value):
			return self.connect(value[0])

		value = re.findall('^guess\s([RGBYOPCMrgbyopcm]{8})$', inputMessage)
		if (value and self.game_key is not None):
			return self.guess(value[0])

		value = re.findall('^hint$', inputMessage)
		if (value and self.game_key is not None and self.pastResults is not None):
			return self.hint()

		value = re.findall('^help$', inputMessage)
		if (value):
			return self.help()

		return "Not Recognized.\nType 'help' to see available commands."

	def connect (self, user):
		jsonResponse = self.game_api.connect(user)
		self.game_key = jsonResponse.get('game_key', None)
		if (self.game_key is not None):
			return "Game Started!"
		return "Game did not start."

	def guess (self, code):
		jsonResponse = self.game_api.guess(code.upper(), self.game_key)
		solved = jsonResponse.get('solved', "false")
		if (solved == "true"):
			message = "You win! It took you " + str(jsonResponse['time_taken']) + " time units to solve it!"
			message += "\n\n" + json.dumps(jsonResponse)
			return message
		result = jsonResponse.get('result', None)
		if (result is not None):
			self.guessHistory = jsonResponse
			return "Exact: " + str(result['exact']) + "\nNear: " + str(result['near'])
		return "Guess not accounted."

	def help (self):
		commands = "start username: Initiates a new game. "
		commands += "Username can contain leters and spaces up to 20 characters.\n\n"
		commands += "guess rgbyopcm: Make a guess on the last initiated game.\n\n"
		commands += "help: Shows this help."
		return commands

		
	def hint (self):
		num_guesses = self.guessHistory['num_guesses']
		past_results = self.guessHistory['past_results']
		hintmap = []
		lastGuess = past_results[num_guesses-1]
		rightPinsLastGuess = lastGuess['exact'] + lastGuess['near']
		for i in range(0,num_guesses-2):
			guessI = past_results[i]
			rightPins = guessI['exact'] + guessI['near']
			if (rightPins < 8):
				# Change n = 8 - rightPints
				# Which n?
				
				pass

		return "Opsie!"
		
		
		
		
