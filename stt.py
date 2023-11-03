# taken the code from Google BARD

# import sys
# sys.path.append('c:\\users\\admin\\appdata\\local\\programs\\python\\python311\\lib\\site-packages')
def convt():
	import speech_recognition as sr
	r = sr.Recognizer() 
	while(1): 
		
		# Exception handling to handle
		# exceptions at the runtime
		try:
			
			# use the microphone as source for input.
			with sr.Microphone() as source2:
				
				# wait for a second to let the recognizer
				# adjust the energy threshold based on
				# the surrounding noise level 
				r.adjust_for_ambient_noise(source2, duration=0.2)
				
				#listens for the user's input 
				audio2 = r.listen(source2,10,10)
				
				# Using google to recognize audio
				MyText = r.recognize_google(audio2)
				MyText = MyText.lower()

				print(MyText)
				return MyText
			
		except sr.WaitTimeoutError:
			print("listening timed out while waiting for phrase to start")
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
		except sr.UnknownValueError:
			print("unknown error occurred")
			
