from deep_translator import GoogleTranslator

def safe_translate(text, target):
    try:
        return GoogleTranslator(source='auto', target=target).translate(text)
    except Exception:
        return text

#----------------------------------------------------------------
# USER INPUTS HIS/HER LANGUAGE
print("""Quelle est ta langue? (eg. anglais, espagnol, allemagne)
What is your language? (e.g. french, arabic, spanish)
أدخل النص الذي تريد ترجمته""")
user_lang_raw = input("> ")
#----------------------------------------------------------------

#---------------------------------------------------------------------------------------------
# TRANSLATES THE USER'S LANGUAGE TO ENGLISH
user_lang = safe_translate(user_lang_raw, target='english').lower()
#---------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------
# USER INPUTS THE TEXT
prompt1 = safe_translate("Enter the text you want to translate:", target=user_lang)
text = input(prompt1 + " ")
#-------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------
# USER INPUTS HIS/HER DESIRED LANGUAGE
prompt2 = safe_translate("Enter your target language:", target=user_lang)
target = input(prompt2 + " ")
#---------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------
# TRANSLATES THE USER'S LANGUAGE TO ENGLISH
target = safe_translate(target, 'english').lower()
#-----------------------------------------------------------------------------------


#----------------------------------------------------------------------
# TRANSLATES THE TEXT TO THE USER'S DESIRED LANGUAGE
result = GoogleTranslator(source='auto', target=target).translate(text)
#----------------------------------------------------------------------


#--------------------------------------------------------------------------------------
# OUTPUTS THE TRANSLATED TEXT
label = safe_translate("Translated text:", target=user_lang)
print(label, result)
#--------------------------------------------------------------------------------------