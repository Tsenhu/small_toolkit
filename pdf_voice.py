# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:51:04 2023

@author: tsenh
"""
import os
from gtts import gTTS
import PyPDF2

def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
        return text

def text_to_speech(text, output_mp3_path, language='en', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save(output_mp3_path)