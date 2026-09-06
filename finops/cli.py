import argparse
from .analytics import load, report

def main():
    p=argparse.ArgumentParser(); p.add_argument('command',choices=['analyze']); p.add_argument('path'); p.add_argument('--output')
    a=p.parse_args(); text=report(load(a.path)); print(text)
    if a.output: open(a.output,'w',encoding='utf-8').write(text)
if __name__=='__main__': main()
