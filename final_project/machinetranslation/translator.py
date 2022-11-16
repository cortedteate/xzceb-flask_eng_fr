import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def eng_2_fre(engtext):
    #write the code here
    translation = language_translator.translate(
    text=engtext,
    model_id='en-fr').get_result()
    print(translation)
    frentext = translation['translations'][0]['translation']
    return frentext

def fre_2_eng(frentext):
    #write the code here
    translation = language_translator.translate(
    text=frentext,
    model_id='fr-en').get_result()
    print(translation)
    engtext = translation['translations'][0]['translation']
    return engtext
