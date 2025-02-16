import requests

class Service:
    WIKIMEDIA_INGREDIENTS_API_URL = "https://en.wikibooks.org/w/api.php?action=query&generator=categorymembers&gcmtitle=Category:Ingredients&gcmlimit=max&gcmnamespace=102&format=json&gcmcontinue="
    
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