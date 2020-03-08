import os, sys
import re
import argparse
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage
import requests
from bs4 import BeautifulSoup
import lxml


db = None
fib = Query()
def init():
  global db
  ref_url = 'http://www.protocol5.com/Fibonacci'
  db = TinyDB(os.path.join(os.getcwd(), 'db.json'), default_table='fibonacci')
  if not len(db):
    resp = requests.get(ref_url)
    soup = BeautifulSoup(resp.text, 'lxml')
    fibonacci_data = soup.find('div',attrs={'class':'fibonacci'})
    links = fibonacci_data.findAll('a')
    for a in links:
      idx = re.search(r'\d+', a['href']).group()
      fib_num = a.contents[0]
      db.insert({'idx': idx, 'num': fib_num})


def check_num(idx, num):
  return len(db.search((fib.idx == str(idx)) & (fib.num == str(num)))) > 0


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('--file', '-f', type=str, help="Use a file as input (Each line has a pair idx fibonacci seperated by space)")
  group.add_argument('--inline', '-i', metavar='N', type=int, nargs=2, help='Check a pair index and fibonacci Number')
  parser.add_argument('--silence', '-s', action='store_true', help="Silence output")
  args = parser.parse_args()

  if (args.file and os.path.isfile(args.file)) or len(sys.argv) >= 3:
    init()

  if args.file:
    with open(args.file) as file:
      for line in file:
        idx, num = line.rstrip('\n').split(' ')
        rtn = check_num(idx, num)
        if not args.silence:
          print(idx, rtn)
  else:
    rtn = check_num(args.inline[0], args.inline[1])
    if not args.silence:
      print(args.inline[0], rtn)

else:
  init()