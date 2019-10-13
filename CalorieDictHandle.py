def csv2dict():
    """turns the csvfile to a list of dictionaries."""
    listOfdicts = list()
    with open(CSVFILE,'r') as fin:    
        for line in fin:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            (food,unit,calUnit,calOunce,calHG) = line.split(",")
            d = dict() 
            d['food'] = food
            d['unit']= unit 
            d['calUnit']= int(calUnit)
            d['calOunce']= int(calOunce)
            d['calHG']= int(calHG) #100g
            listOfdicts.append(d)             
    
    return listOfdicts 

def dictChangeUnit():
    """ changes the original dictionary units to fit the recipe."""
    dicts = csv2dict()
    copyOfdicts = dicts
    listOfChangedDicts = list()
    for d in copyOfdicts:
        if d['unit'] == 'tsp':
            d['unit'] = 'teaspoon'
        if d['unit'] == 'tbsp':
            d['unit'] = 'tablespoon'
        listOfChangedDicts.append(d)
    
    return listOfChangedDicts          