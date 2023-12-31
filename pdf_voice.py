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
import shutil

path = 'c:/Users/tsenh/GitHub/'

input_pdf_path = path + 'input_test/50YearsDataScience.pdf'
output_mp3_path = path + "output_test/50YearsDataScience.mp3"
temp_folder = path + 'input_test/temp/'    

#clean the temp_folder first
mp3_list = os.listdir(temp_folder)

for m in mp3_list:
    
    os.unlink(temp_folder+m)
    
    
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
        audio_data.save(temp_folder+str(page_num)+'.mp3')
        print('Page {} has been processed.'.format(page_num))
        t.sleep(10)



mp3_list = os.listdir(temp_folder)

combined_audio = AudioSegment.from_mp3(temp_folder+mp3_list[0])

for mp3 in mp3_list[1:]:
    combined_audio += AudioSegment.from_mp3(temp_folder+mp3)


combined_audio.export(output_mp3_path, format='mp3')        
