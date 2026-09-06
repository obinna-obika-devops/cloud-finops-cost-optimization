#!/usr/bin/env python3
import sys
import pandas as pd
from finops.analytics import load

def main():
    df=load('data/sample/cost_usage.csv')
    required={'team','environment','cost_center'}
    missing=required-df.columns
    if missing:
        print(f'FAIL: missing allocation fields: {sorted(missing)}'); return 1
    daily=df.groupby('date').cost_usd.sum()
    if daily.empty or (daily<0).any():
        print('FAIL: invalid cost data'); return 1
    print(f'PASS: {len(df)} cost records validated; spend=${df.cost_usd.sum():,.2f}')
    return 0
if __name__=='__main__': sys.exit(main())
