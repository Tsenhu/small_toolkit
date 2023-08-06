# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:51:04 2023

@author: tsenh
"""
import os
from gtts import gTTS
import PyPDF2
import time as t

path = 'c:/Users/tsenh/GitHub/'

def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def text_to_speech(text, output_mp3_path, language='en', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save(output_mp3_path)
    
if __name__ == "__main__":
    input_pdf_path = path + 'input_test/50YearsDataScience.pdf'
    output_mp3_path = path + "output_test/50YearsDataScience.mp3"
    
    text = extract_text_from_pdf(input_pdf_path)
    text_to_speech(text, output_mp3_path= output_mp3_path)