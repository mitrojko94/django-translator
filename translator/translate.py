from random import random
import random
from googletrans import Translator

def translate(text):
    translator = Translator()

    translation_fr = translator.translate(text=text, dest="fr")
    translation_de = translator.translate(text=text, dest="de")
    return translation_fr.text + "\n" + translation_de.text
