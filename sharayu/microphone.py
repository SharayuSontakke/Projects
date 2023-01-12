import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone(device_index=0) as source:
    print("say something...") 
    audio=r.listen(source)
    query=r.recognize_google(audio)
    print(query)