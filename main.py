from datetime import datetime
import subprocess
import os

cwd = os.path.dirname(os.path.realpath(__file__))

data = {
  'sun': [0,1,1,0,0,0,0,0,0,0,0,0,0,0],
  'mon': [1,0,0,1,0,0,0,0,0,0,0,1,0,0],
  'tue': [1,0,0,1,1,1,1,1,1,1,1,1,1,0],
  'wen': [0,1,1,1,0,0,0,0,0,0,0,0,1,1],
  'thu': [1,0,0,1,1,1,1,1,1,1,1,1,1,0],
  'fri': [1,0,0,1,0,0,0,0,0,0,0,1,0,0],
  'sut': [0,1,1,0,0,0,0,0,0,0,0,0,0,0],
}

def makeCommit():
  filename = 'commitfile'
  with open(filename, 'a+', encoding='utf-8') as file:
    file.write('Today in a wary good %s\n' % (datetime.today().strftime('%A %B %d')))

  gitAdd(filename)
  gitCommit()
  #gitPush()

def gitAdd(fileName):
    cmd = ['git', 'add', fileName]
    p = subprocess.Popen(cmd, cwd=cwd)
    p.wait()

def gitCommit():
  cmd = ['git', 'commit', '-m', '"Update data"']
  p = subprocess.Popen(cmd, cwd=cwd)
  p.wait()

def gitPush():
  cmd = ['git', 'push', 'origin', 'main']
  p = subprocess.Popen(cmd, cwd=cwd)
  p.wait()

startWeek = 14
weekCounter = int(datetime.today().strftime('%W')) - startWeek
nowDay = datetime.today().strftime('%a').lower()

if data[nowDay][weekCounter] == 1:
  makeCommit()