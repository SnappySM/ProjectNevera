import requests
from deep_translator import GoogleTranslator

class Service:
    WIKIMEDIA_INGREDIENTS_API_URL = "https://en.wikibooks.org/w/api.php?action=query&generator=categorymembers&gcmtitle=Category:Ingredients&gcmlimit=max&gcmnamespace=102&format=json&gcmcontinue="
    translator = GoogleTranslator(source="en", target="ca")
    
    @staticmethod
    def process_ingredients(ingredients):
        result = []
        for ingredient in ingredients:
            ingredient_en = ingredients[ingredient]["title"].replace("Cookbook:", "")
            result.append(ingredient_en)
        return result

    def get_key_terms(self):
        url = self.WIKIMEDIA_INGREDIENTS_API_URL
        response =  requests.get(url)
        key_terms = response.json()
        ingredients = key_terms["query"]["pages"]
        result = []
        result += self.process_ingredients(ingredients)
        while not (key_terms.get("continue") is None):
            url = self.WIKIMEDIA_INGREDIENTS_API_URL + key_terms["continue"]["gcmcontinue"]
            response =  requests.get(url)
            key_terms = response.json()
            ingredients = key_terms["query"]["pages"]
            result += self.process_ingredients(ingredients)
        return result
    
    # Translator at 100 chars seems to be reliable for spanish, not catalan
    def translate_array(self, array):
        stringified_array = ", ".join(array)
        strings_to_translate = []
        while len(stringified_array) > 100:
            i = 100
            while stringified_array[i] != ",":
                i -= 1
            strings_to_translate.append(stringified_array[:i])
            stringified_array = stringified_array[i+2:]
        strings_to_translate.append(stringified_array)
        translated_ca = []
        translated_es = []
        for element in strings_to_translate:
            self.translator.target = "ca"
            translated_ca += self.translator.translate(text=element).split(", ")
            self.translator.target = "es"
            translated_es += self.translator.translate(text=element).split(", ")
        return [translated_ca, translated_es]