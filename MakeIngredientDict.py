def reformat(calculableSet):
    """ reformat the calculable set to be able to create a dictionary later 
        ,for example " 2 cups of unsalted butter(room temperaure)" => "2 cup unsalted butter"
    """
    formatedSet = set()
    COMMA = ','
    LPAREN = '('
    RPAREN = ')'
    removingWords = ['of','fresh','melted','large','small','dry']
    for item in calculableSet:
        if 'plus' in item:
             continue
        if '+' in item:
             continue 
        if 'tablespoons' in item:
            item = item.replace('tablespoons','tablespoon')
        if 'teaspoons' in item:
            item = item.replace('teaspoons','teaspoon')  
        if 'cups' in item:
            item = item.replace('cups','cup')   
        if 'ounces' in item:
            item = item.replace('ounces','ounce') 
        if LPAREN in item:
            indexL = item.index(LPAREN)
            indexR = item.index(RPAREN)
            item = item[:LPAREN]+item[RPAREN+1:]
        if 'to' in item:
            item = item.replace('to',COMMA)
            item = item[0:item.index(COMMA)]
        for removingWord in removingWords:
            if removingWord in item:
                item = item.replace(removingWord,'')
        if 'egg yolks' in item:
            item = item.replace('egg yolks','egg-yolk')
            item = item +' '+ 'egg yolk'
        if 'egg whites' in item:
            item = item.replace('egg whites','egg-white')
            item = item +' '+ 'egg white'
        if 'eggs' in item:
            item = item +' '+'eggs' 
        formatedSet.add(item)
    return formatedSet

def getFood(ingredient,unit): 
    foods = list()
    SPACE = " " 
    for i in range(ingredient.index(unit)+1,len(ingredient)):
        foods.append(ingredient[i])
    food = SPACE.join(foods)
                  
    return food
from fractions import Fraction

# get the number before unit

def getMeasurement(ingredient,unit):
    numbers = list()
    for i in range(0,ingredient.index(unit)):
        numbers.append(ingredient[i])
    measurement= float(sum(Fraction(number) for number in numbers))

UNITS = ['cup','teaspoon','tablespoon','gram','ounce','eggs','egg-white','egg-yolk']
formatedSet = reformat(calculableSet)

def formatedSet2dicts(formatedSet):
    unpackedSet = set()
    formatedIngreDicts = list()
    keys = ('food','measurement','unit')
    for ingredient in formatedSet:
        ingredient = ingredient.split()
        d = dict()
        for unit in UNITS:
            for item in ingredient:
                if unit == item:
                    food = getFood(ingredient,unit)
                    measurement = getMeasurement(ingredient,unit)
                    t = (food,measurement,unit)
                    if t:
                        unpackedSet.add(t)
   
    for t in unpackedSet:
        d = dict(zip(keys,t))
        formatedIngreDicts.append(d)
    return formatedIngreDicts
    
    return measurement