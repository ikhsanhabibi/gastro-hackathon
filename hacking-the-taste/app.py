from flask import Flask
from flask import request
import ast
import csv
import mysql.connector
import json
app = Flask(__name__)
  
@app.route('/flotest')
def say_hello():
  a = {'name':'Sarah', 'age': 24, 'isEmployed': True }
  return a

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data = request.data
    print(data)
    return('hallo')


@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    website = request.args.get('website')
    a = {'name':language, 'framework': framework, 'website': website }
    return a

@app.route('/allergentest', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'

@app.route('/allergene', methods = ['POST'])
def postJsonHandler2():
  print('Following data recieved: ')
  req_data = request.get_data(as_text=True)
  allergene_results = check_allergene(req_data)
  return allergene_results

def getcontaminatedfood2(linevalue):
 """  print('connecting to database')
  my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    db="gastrohack"
  )
  print('connected to database')
  mycursor = my_db.cursor()
  tocheck = "'Schnitzel','Brot'"
  mycursor.execute("SELECT Allergen FROM matching_allergene WHERE Gericht IN ('Schnitzel','Brot');")
  for x in mycursor:
    print(x) 
    return(['2','5'])"""

def getcontaminatedfood3(linevalue):
  with open('matching_allergene.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}

def getcontaminatedfood(linevalue):
  if("Milch" in linevalue or "Eiskaffee" in linevalue):
    return(['7'])
  elif("Brotchen"in linevalue):
      return(['1'])
  elif("Brot"in linevalue):
      return(['1'])
  elif("Brötchen"in linevalue):
      return(['1'])
  elif("Müsli"in linevalue):
      return(['1'])
  elif("Spiegeleier"in linevalue):
      return(['3'])
  elif("Musli"in linevalue):
      return(['1'])
  elif("Nudel"in linevalue):
      return(['1'])
  elif("Jägerschnitzel"in linevalue):
    return(['1'])
  elif("Weizen"in linevalue):
    return(['1'])
  elif("Gerste"in linevalue):
    return(['1'])
  elif("Burger"in linevalue):
    return(['1'])
  elif("Bier"in linevalue):
    return(['1'])
  elif("Pils"in linevalue):
    return(['1'])
  elif("Spaghetti"in linevalue):
    return(['1'])
  elif("Strudel"in linevalue):
    return(['1','3'])
  elif("Kaiserschmarren"in linevalue):
    return(['1','3'])
  elif("Sahne"in linevalue):
    return(['7'])
  elif("Schnitzel"in linevalue):
    return(['2','4','7'])
  elif("Flusskrebsen"in linevalue):
   return(['14'])
  elif("Tintenfische"in linevalue):
    return(['14'])
  elif("Muscheln"in linevalue):
    return(['14'])
  elif("Schnecken"in linevalue):
    return(['14'])
  elif("Lupinen"in linevalue):
    return(['13'])
  elif("Weißwein"in linevalue):

   return(['12'])

  elif("Rotwein"in linevalue):

   return(['12'])

  elif("Wein"in linevalue):

   return(['12'])

  elif("Sulfite"in linevalue):

   return(['12'])

  elif("Schwefeldioxid"in linevalue):

   return(['12'])

  elif("Sesamsamen"in linevalue):

   return(['11'])

  elif("Senfsauce"in linevalue):

   return(['10'])

  elif("Senf"in linevalue):

   return(['10'])

  elif("Sellerie"in linevalue):

   return(['9'])

  elif("Paranuss"in linevalue):

   return(['8'])

  elif("Pekannuss"in linevalue):

   return(['8'])

  elif("Cashewnuss"in linevalue):

   return(['8'])

  elif("Walnuss"in linevalue):

   return(['8'])

  elif("Haselnuss"in linevalue):

   return(['8'])

  elif("Mandel"in linevalue):

   return(['8'])

  elif("Pistazie"in linevalue):

   return(['8'])

  elif("Queenslandnuss"in linevalue):

   return(['8'])

  elif("Macadamianuss"in linevalue):

   return(['8'])

  elif("Paranüsse"in linevalue):

   return(['8'])

  elif("Pekannüsse"in linevalue):

   return(['8'])

  elif("Cashewnüsse"in linevalue):

   return(['8'])

  elif("Walnüsse"in linevalue):

   return(['8'])

  elif("Haselnüsse"in linevalue):

   return(['8'])

  elif("Butter"in linevalue):

   return(['7'])

  elif("Obazda"in linevalue):

   return(['7'])

  elif("Sauerrahm"in linevalue):

   return(['7'])

  elif("Brie"in linevalue):

   return(['7'])

  elif("Tiramisu"in linevalue):

   return(['7'])

  elif("Heiße Schokolade"in linevalue):

   return(['7'])

  elif("Trinkschokolade"in linevalue):

   return(['7'])

  elif("Schmand"in linevalue):

   return(['7'])

  elif("Quark"in linevalue):

   return(['7'])

  elif("Mascaporne"in linevalue):

   return(['7'])

  elif("Laktose"in linevalue):

   return(['7'])

  elif("Büffelmozarella"in linevalue):

   return(['7'])

  elif("Buffelmozarella"in linevalue):

   return(['7'])

  elif("Mozarella"in linevalue):

   return(['7'])

  elif("Ziegenkase"in linevalue):

   return(['7'])

  elif("Ziegenkäse"in linevalue):

   return(['7'])

  elif("Eis"in linevalue):

   return(['7'])

  elif("Schlagsahne"in linevalue):

   return(['7'])

  elif("Eiskaffee"in linevalue):

   return(['7'])

  elif("Expresso Machiato"in linevalue):

   return(['7'])

  elif("Latte Machiato"in linevalue):

   return(['7'])

  elif("Milchkaffee"in linevalue):

   return(['7'])

  elif("Cappuccino"in linevalue):

   return(['7'])

  elif("Naturjoghurt"in linevalue):

   return(['7'])

  elif("Joghurt"in linevalue):

   return(['7'])

  elif("Yoghurt"in linevalue):

   return(['7'])

  elif("Käse"in linevalue):

   return(['7'])

  elif("Kässe"in linevalue):

   return(['7'])
  elif("Soja"in linevalue):

   return(['6'])

  elif("Sojabohnen"in linevalue):

   return(['6'])

  elif("Sojamilch"in linevalue):

   return(['6'])

  elif("Erdnuss"in linevalue):

   return(['5'])

  elif("Milch"in linevalue):

   return(['7'])

  elif("Seezunge"in linevalue):

   return(['4'])

  elif("Fischgelatine"in linevalue):

   return(['4'])

  elif("Fisch"in linevalue):

   return(['4'])

  elif("Fischstäbchen"in linevalue):

   return(['4'])

  elif("Fischstabchen"in linevalue):

   return(['4'])

  elif("Omelette"in linevalue):

   return(['3'])

  elif("Eiern"in linevalue):

   return(['3'])

  elif("Eier"in linevalue):

   return(['3'])

  elif("Ei"in linevalue):

   return(['3'])

  else:
    return([])

def check_allergene(req_data):
  #try:
    #print(type(req_data))
    my_dict=json.loads(req_data)
    print(type(my_dict))
    print("raw dict recieved: ")
    print(my_dict)
    myreturndict={}
    #print("---------------------------")
    for blockKey in my_dict:
      block = my_dict[blockKey]
      myreturnblock={}
      for lineKey in block:
        line = block[lineKey] 
        print("Block: " +blockKey+ " Line: " +str(lineKey)+ " " + str(line))
        allergene = getcontaminatedfood(line)
        allergene_count = int(len(allergene))
        if int(allergene_count > 0):
          myreturnblock[lineKey]=allergene
      myreturndict[blockKey]=myreturnblock
    return myreturndict
  #except:
    #print("Error in converting to dict")


def log_msg_in_txt(nachricht):
  with open("log.txt", "a") as x:
    dummy = nachricht + "\n" + "\n"
    x.write(dummy)

# if __name__ == "__main__":
#   print("Einstiegspunkt")  
#   getcontaminatedfood()