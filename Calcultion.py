def calculate(ingreDicts,dictsForCalculate):
    calories = []
    calorie = 0.0
    for item in ingreDicts:
        for d in dictsForCalculate:
            if item['food'].upper()== d['food'].upper():
                if item['unit'] == d['unit']:
                    calorie = d['calUnit']*item['measurement']
                elif item['unit'] == 'ounce':  
                    calorie = d['calOunce']*item['measurement']
                elif item['unit'] == 'gram':
                    calorie = d['calHG']/100*item['measurement']
                calories.append(calorie)     
    
    return sum(calories)                
                
    
