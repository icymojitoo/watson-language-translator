from ibm_watson import LanguageTranslatorV3     # import language transator from watson
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator      # import authenticator
from decouple import config

"""
This file sets up the Language Translator from the IBM Watson Cloud
"""

URL_LT = config('URL_LT')
APIKEY_LT = config('APIKEY_LT')
VERSION_LT = config('VERSION_LT')
authenticator = IAMAuthenticator(APIKEY_LT) # Authentication

# push the info in a translator variable
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(URL_LT)
