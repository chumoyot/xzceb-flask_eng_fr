from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    ''' This function translates english to french.'''

    french_text = MyMemoryTranslator(source='en-AU', target='fr-FR').translate(english_text)
    return french_text
def french_to_english(french_text):
    '''This function translates french to english.'''

    english_text = MyMemoryTranslator(source='fr-FR', target='en-AU').translate(french_text)
    return english_text
