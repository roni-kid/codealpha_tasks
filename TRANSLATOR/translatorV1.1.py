from deep_translator import GoogleTranslator

#----------------------------------------------------------------
# USER INPUTS HIS/HER LANGUAGE
print("""Quelle est ta langue? (eg. anglais, espagnol, allemagne)
What is your language? (e.g. french, arabic, spanish)
أدخل النص الذي تريد ترجمته""")
user_lang_raw = input("> ")
#----------------------------------------------------------------

#---------------------------------------------------------------------------------------------
# TRANSLATES THE USER'S LANGUAGE TO ENGLISH
user_lang = GoogleTranslator(source='auto', target='english').translate(user_lang_raw).lower()
#---------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------
# USER INPUTS THE TEXT
prompt1 = GoogleTranslator(source='auto', target=user_lang).translate("Enter the text you want to translate:")
text = input(prompt1 + " ")
#-------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------
# USER INPUTS HIS/HER DESIRED LANGUAGE
prompt2 = GoogleTranslator(source='auto', target=user_lang).translate("Enter your target language:")
target = input(prompt2 + " ")
#---------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------
# TRANSLATES THE USER'S LANGUAGE TO ENGLISH
target = GoogleTranslator(source='auto', target='english').translate(target).lower()
#-----------------------------------------------------------------------------------


#----------------------------------------------------------------------
# TRANSLATES THE TEXT TO THE USER'S DESIRED LANGUAGE
result = GoogleTranslator(source='auto', target=target).translate(text)
#----------------------------------------------------------------------


#--------------------------------------------------------------------------------------
# OUTPUTS THE TRANSLATED TEXT
label = GoogleTranslator(source='auto', target=user_lang).translate("Translated text:")
print(label, result)
#--------------------------------------------------------------------------------------