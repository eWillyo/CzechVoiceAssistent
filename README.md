# Czech Voice Assistent (ChatGPT)

This small project of voice assistent uses ChatGPT in human's nature way. It's based on Coqui STT and TTS libraries. Third essential library you'll need is 'openai'. This library is a wrapper which sends questions and answears to ChatGPT servers. Due that, you have to be registered on [chat.openai.com] and you'll need to paste to 'MyOpenAI.py' file your API key (YOUR_API_KEY). Here are instructions: [https://www.codingthesmartway.com/how-to-use-chatgpt-with-python/]. 

# Requirements

Except Coqui TTS and TTS libraries (and 'openai' library) installed standard way via 'pip', you need following dependencies: 

     pyaudio, webrtcvad, halo, num2words
     
Also install 'aplay' from linux repositories (if you don't have it on your system).

Note: There can be some problems with 'Numpy's version during TTS instalation due to which script may not works. Solution is upgrade numpy and numba after installation of all libraries:

     pip install --upgrade numpy
     pip install --upgrade numba
     
One of last things you'll need is czech language model for STT library (Czech STT v0.3.0). Download it from here: [https://coqui.ai/models]. You'll need 'kenlm.scorer' and 'model.tflite' files. Place them to directory with project.  
     
And of course you'll need microphone :-)




Currently code works only on Linux (I use 'aplay' Linux player in code to play "text to words"). I work on that - I promiss!
