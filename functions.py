from translator import language_translator  # import the translation module

"""
Translator Functions
"""

def to_french(translate):
    """
    Translates English string input to French
    """
    french_translation = language_translator.translate(text=translate, model_id='en-fr').get_result()
    return french_translation['translations'][0]['translation']     # output French translation value

def to_german(translate):
    """
    Translates English string input to German
    """
    german_translation = language_translator.translate(text = translate, model_id = 'en-de').get_result()
    return german_translation['translations'][0]['translation'] # output German translation value