#Import packageds/modules
import argparse

#This function will return all command line arguemnts as an object
def get_args():

  #Initalize an argparser object. Documentation on the argparser module is here: 
  #https://docs.python.org/3/library/argparse.html
  argparser = argparse.ArgumentParser()
  
  #Add ability for user to specify that they want to use SQLite, instead of MySQL database
  #Also, lets user specify the name and path of the SQLite DB file to use
  argparser.add_argument('-l','--lite',help = "use -l or --lite to connect to sqlite DB, otherwise use MySQL DB", type=str, default=None)
  
  #Boolean arguement of using TEST MySQL DB or the main MySQL DB
  argparser.add_argument('--test_database', action='store_true', default=False, help='Use testing database (MySQL)')
  
  #Convert the arguement strings into attributes of the namespace
  args = argparser.parse_args()

  return args
