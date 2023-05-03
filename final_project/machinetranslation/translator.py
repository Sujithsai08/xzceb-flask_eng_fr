import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator=IAMAuthenticator(apikey)
language_translator=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    Translate English text to French using IBM Watson Language Translator API.
    """
    # write the code here
    if englishText is None or len(englishText) <= 0:
        return ''
    translation = dict(
        language_translator.translate(text=englishText, model_id='en-fr').get_result()
    )
    return translation["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    """
    Translate frenchtext to english using IBM Watson Language Translator API.
    """
    # write the code here
    if frenchText is None or len(frenchText)<=0:
        return ''
    translation = dict(
        language_translator.translate(text=frenchText, model_id='fr-en').get_result()
        )
    return translation["translations"][0]["translation"]