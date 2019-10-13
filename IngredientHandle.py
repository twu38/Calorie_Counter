import re

def getWholeIngreSet(recipe):
    """ find the common pattarn for calculable ingredients which usually start with a number
        , for example: '1 cup unsalted butter' 
    """
    pat = "[0-9]"
    COMMA = ','
    RECIPE = recipe
    wholeIngreSet = set()
    with open(RECIPE,'r') as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            if COMMA in line:
                line = line[:line.index(COMMA)]
            if re.match(pat,line):
                wholeIngreSet.add(line) 
        return wholeIngreSet   
    
def getCalculableSetAndDicts(wholeIngreSet):
    """ uses the dictionary to select calculable ingredients and saves the dictionary we've used."""
    calculableSet = set()
    unitChangedDicts = dictChangeUnit()
    dictsForCalculate = list()
    for item in wholeIngreSet:
        for d in dicts:
            if d['food'].upper() in item.upper() and d['unit'] in item:
                calculableSet.add(item)
                dictsForCalculate.append(d) 
            elif d['food'] in item and 'ounce' in item:    
                calculableSet.add(item)
                dictsForCalculate.append(d) 
            elif d['food'] in item and 'gram' in item:
                calculableSet.add(item)
                dictsUsedForCalculate.append(d) 
    return [calculableSet,dictsForCalculate] 

setAndDicts = getCalculableSetAndDicts(wholeIngreSet)
calculableSet,dictsForCalculate = setAndDicts 

def getNotCalculableSet(wholeIngreSet,calculableSet):
    return wholeIngreSet - calculableSet
   
