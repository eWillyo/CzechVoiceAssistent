immport re

from pathlib import Path
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
from TTS.api import TTS

#import numbers
from num2words import num2words

from playsound import playsound


model_name_tts = "tts_models/cs/cv/vits" #czech
#model_name_tts = "tts_models/multilingual/multi-dataset/your_tts"

class MyTTS:
    def __init__(self, model_name):
        self.model_name = model_name
        self.synthesizer = None
        
    def init_TTS(self):
        print('Initializing TTS model...')

        path = Path(__file__).parent / "models.json"
        manager = ModelManager(path)
        model_path, config_path, _ = manager.download_model(self.model_name)
        self.synthesizer = Synthesizer(model_path, config_path)
    
    def say_something(self, txt):
        wav = self.synthesizer.tts(self.nm2ws(txt))
        self.synthesizer.save_wav(wav, ".temp.wav")
        playsound(".temp.wav")
        
    def nm2ws(self, text):
        result = []
        
        for t in text.split():
            is_not_text, has_point, is_decimal = self.get_num_type(t)

            try:
                if is_not_text and not is_decimal and not has_point:
                    t = num2words((int)(t), lang='cz')
                
                if is_not_text and has_point and not is_decimal:
                    t = t.replace('.', '')
                    t = num2words((int)(t), lang='cz')#, to='ordinal')
                
                if is_not_text and is_decimal:
                    t = num2words((float)(t), lang='cz')
                
            except ValueError:
                pass
            
            result.append(t)
            
        return ' '.join(result)
    
    def get_num_type(self, word):
        is_not_text = True
        has_point = False
        is_decimal = False
        
        for c in word:
            if c == '.':
                has_point = True
                continue
            
            if c.isdigit() == False:
                is_not_text = False
                break
            
            if c.isdigit() == True:
                is_not_text = True
                if has_point == True:
                    is_decimal = True
                    
        return (is_not_text, has_point, is_decimal)
                
                
