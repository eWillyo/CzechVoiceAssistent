#!/usr/bin/env python

import MySTT
import MyTTS
import MyOpenAI

import random

INIT_PHRASE = "Hlasový asistent Malina je připraven"
WAKE_UP_PHRASES = ["malino", "malina"]

ANSWEAR_PHRASES = ["Ano?", "Poslouchám...", "Co si přeješ?", "S čím ti můžu pomoct?", "Co potřebuješ?", "Máš dotaz?"]


tts = MyTTS.MyTTS(MyTTS.model_name_tts)
stt = MySTT.MySTT(MySTT.model_name_stt, MySTT.scorer_stt, MySTT.VAD_stt)
openAI = MyOpenAI.MyOpenAI(MyOpenAI.model_to_use, MyOpenAI.API_KEY)


def answear(text):
    (res, usage) = openAI.chatGPT(text)
    tts.say_something(res)
    return True
    

def respawn(text):
    if text == WAKE_UP_PHRASES[0] or text == WAKE_UP_PHRASES[1]:
        tts.say_something(ANSWEAR_PHRASES[random.randrange(len(ANSWEAR_PHRASES))])
        stt.listening_STT()
        stt.listening_STT(answear)
        return False

if __name__ == "__main__":
    tts.init_TTS()
    stt.init_STT()
    
    tts.say_something(INIT_PHRASE)
    #print(tts.nm2ws("Jan Hus byl upálen 6. července 1415"))
    #print(tts.nm2ws("9 děleno 8 je 1.125"))
    
    try:
        while True:
            stt.listening_STT(respawn)
    except ValueError as e:
        print(e)
        exit(-1)


