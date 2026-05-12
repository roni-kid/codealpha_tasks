from deep_translator import GoogleTranslator

#-----------------------------------------------------
# USER INPUT
text = input("Enter the text you want to translate: ")
language = input("Enter your desired language: ")
#-----------------------------------------------------

#------------------------------------------------------------------------------
# TRANSLATION PROCESS
translator = GoogleTranslator(source='auto', target=language).translate(text)
translated = translator
#------------------------------------------------------------------------------

#-------------------------------------
# OUTPUT
print("Translated text: ", translated)
#-------------------------------------