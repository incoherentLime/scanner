import subprocess
import argparse 
parser = argparse.ArgumentParser(description='finds the subdomains')
parser.add_argument('subdomain',metavar='subs',type=str,help='enter a subdomain')
args = parser.parse_args()
url = args.subdomain

process = subprocess.Popen(["/home/lime/go/bin/assetfinder", "--subs-only", url],text=True,stdout=subprocess.PIPE) 
while True:
  line = process.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  print( "test:", line.rstrip())