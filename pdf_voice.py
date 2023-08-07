# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:51:04 2023

@author: tsenh
"""
import os
from gtts import gTTS
import PyPDF2
import time as t
from pydub import AudioSegment
import os
import io


path = 'c:/Users/tsenh/GitHub/'

input_pdf_path = path + 'input_test/renter insurance.pdf'
output_mp3_path = path + "output_test/renter insurance.mp3"
temp_folder = path + 'input_test/temp/'    
def text_to_speech(text, language='en', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    return tts   
    
with open(input_pdf_path, 'rb') as file:
    
    pdf_reader = PyPDF2.PdfReader(file)
    
    text = ''
    audio_segments = []
    for page_num in range(len(pdf_reader.pages)):
        
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        '''
        audio_segment = text_to_speech(text, language='en', slow=False)
        audio_segments.append(AudioSegment.from_file(os.path.devnull, format="mp3", frame_rate=44100, channels=2, sample_width=2, data=audio_segment))
        '''
        audio_data = text_to_speech(text, language = 'en', slow=False)
        audio_segment = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
        audio_segments.append(audio_segment)
        
combined_audio = audio_segments[0]
for audio_segment in audio_segments[1:]:
    combined_audio += audio_segment
        
audio_segment.save(combined_audio, output_mp3_path)