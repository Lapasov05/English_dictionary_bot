import requests
import googletrans
from langdetect import detect, detect_langs
from googletrans import Translator

translator = Translator()

import requests

def get_main_word(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    r = requests.get(url)
    res = r.json()
    output = {}

    definitions = []
    if res and isinstance(res, list) and res[0] and 'meanings' in res[0] and res[0]['meanings'][0] and 'definitions' in res[0]['meanings'][0]:
        senses = res[0]['meanings'][0]['definitions']
        for sense in senses:
            if 'definition' in sense:
                definitions.append(f"👉 {sense['definition']}")
    else:
        return False
    output['definitions'] = "\n".join(definitions)
    if 'phonetics' in res[0] and 'audio' in res[0]['phonetics'][0]:
        output['audio'] = res[0]['phonetics'][0]['audio']
    else:
        output['audio'] = "Sorry, an audio pronunciation is not available."
    return output



from mtranslate import translate

import langid

def detect_language(text):
    detected_lang, _ = langid.classify(text)
    print(detected_lang)
    return detected_lang


def translate_text(text,):
    target_lang=detect_language(text)
    if target_lang == 'en':
        target_lang = 'uz'
        translated_text = translate(text, target_lang)
    else:
        target_lang = 'en'
        translated_text = translate(text, target_lang)
    return translated_text

def translate_text_uz(text):
    translated_text = translate(text, 'uz')
    return translated_text




