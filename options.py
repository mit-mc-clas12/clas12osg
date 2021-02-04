import argparse

def get_args():

  argparser = argparse.ArgumentParser()
  
  argparser.add_argument('-l','--lite',help = "use -l or --lite to connect to sqlite DB, otherwise use MySQL DB", type=str, default=None)
  argparser.add_argument('--test_database', action='store_true', default=False, help='Use testing database (MySQL)')
  args = argparser.parse_args()

  return args