from urllib.request import urlopen
from bs4 import BeautifulSoup

RECIPE_OUTFILE ='/Users/apple/Desktop/Calorie_Counter/recipe.txt'
CSVFILE = '/Users/apple/Desktop/Calorie_Counter/nutri_revised.csv'
UNITS = ['cup','teaspoon','tablespoon','gram','ounce','eggs','egg-white','egg-yolk'

def url2html(url):
    """ gives URL and returns html page."""
    UClient = urlopen(url)
    page = UClient.read()
    UClient.close()
    htmlPage = BeautifulSoup(page,"html.parser")
    
    return htmlPage

def url2recipe(url):
    """gives URL ,then retrieves the recipe and returns the filename(path) of the recipe."""
    htmlPage = url2html(url)
    with open(RECIPE_OUTFILE,'w') as fout:
        for item in htmlPage.find_all("p",{"class":"p-ingredient"}):
            print(item.text,file = fout)
    recipe = fout.name
    
    return recipe

def url2title(url):
    """ gives URL and returns the title of the page, for example:

    >>> url2title('https://www.tastemade.com/videos/spring-time-green-tea-mousse-cake')
    'Spring Time Green Tea Mousse Cake ~ Recipe | Tastemade'
    """
    htmlPage = url2html(url)
    title = htmlPage.title.text   
    
    return title
