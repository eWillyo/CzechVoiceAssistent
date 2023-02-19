# Czech Voice Assistent (ChatGPT)

This small project of voice assistent uses ChatGPT in human's nature way. It's based on Coqui STT and TTS libraries. Third essential library you'll need is 'openai'. This library is a wrapper which sends questions and answers to ChatGPT servers. Due that, you have to be registered on [https://chat.openai.com/] and you'll need to paste to 'MyOpenAI.py' file your API key (YOUR_API_KEY). 
Here are instructions: [https://www.codingthesmartway.com/how-to-use-chatgpt-with-python/]. 

# Requirements

Except Coqui's 'tts' and 'stt' libraries (and 'openai' library) installed standard way via 'pip', you'll need following dependencies: 

     pyaudio, webrtcvad, halo, num2words, playsound

Note: There can be some problems with Numpy's version during TTS instalation due to which the script may not work. Solution is upgrade Numpy and Numba after installation of all libraries:

     pip install --upgrade numpy
     pip install --upgrade numba
     
One of the last things you'll need is Czech language model for STT library (Czech STT v0.3.0). Download it from here: [https://coqui.ai/models]. You'll need 'kenlm.scorer' and 'model.tflite' files. Place them to directory with project.  
     
And of course you'll need a microphone :-)




Currently, code works on Linux and Windows, as I promissed.
