from app import app

from flask import render_template
from flask import request
import requests
import os


from .translate import encrypt
from .translate import decrypt


@app.route('/', methods=['GET'])
def index():
	
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    
    original_text = request.form['text']
    target_cypher = request.form['language']
    target_action = request.form['action']
    key = request.form['key']
    
    if target_action == "en":
        translated_text = encrypt(original_text, target_cypher, key)
    else:
        translated_text = decrypt(original_text, target_cypher, key)
    
    if target_cypher == "cae":
        cypher = "Шифр Цезаря"
    elif target_cypher == "vig":
        cypher = "Шифр Виженера"
    else:
        cypher = "Шифр Вернама"
        
    if target_action == "en":
        action = " [Шифрование]"
    else:
        action = " [Дешифрование]"
    
    return render_template(
        'results.html',
        translated_text = translated_text,
        original_text = original_text,
        key = key,
        method = cypher + action
    )
   
