import argparse
from pathlib import Path
import pandas as pd
import numpy as np

def load(path):
    df=pd.read_csv(path, parse_dates=['date'])
    df['cost_usd']=df['cost_usd'].astype(float)
    return df

def analyze(df):
    total=df.cost_usd.sum()
    by_team=df.groupby('team').cost_usd.sum().sort_values(ascending=False)
    by_service=df.groupby('service').cost_usd.sum().sort_values(ascending=False)
    return total,by_team,by_service

def forecast(df, days=30):
    daily=df.groupby('date').cost_usd.sum().sort_index()
    if len(daily)<2: return float(daily.iloc[-1]) if len(daily) else 0
    x=np.arange(len(daily)); slope,intercept=np.polyfit(x,daily.values,1)
    future=np.arange(len(daily),len(daily)+days)
    return max(0,float(np.maximum(0,slope*future+intercept).sum()))

def anomalies(df):
    daily=df.groupby('date').cost_usd.sum().sort_index()
    mean=daily.mean(); std=daily.std(ddof=0)
    if std==0: return daily.iloc[0:0]
    return daily[daily > mean+2*std]

def report(df):
    total,teams,services=analyze(df)
    lines=['# FinOps Demo Report','',f'**Total spend:** ${total:,.2f}','', '## Spend by team','']
    lines += [f'- {k}: ${v:,.2f}' for k,v in teams.items()]
    lines += ['', '## Spend by service','']
    lines += [f'- {k}: ${v:,.2f}' for k,v in services.items()]
    lines += ['', '## Forecast', '', f'- Estimated next 30 days: ${forecast(df):,.2f}', '', '## Anomalies', '']
    hits=anomalies(df)
    lines += [f'- {d.date()}: ${v:,.2f}' for d,v in hits.items()] or ['- None detected']
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='cmd',required=True)
    for name in ['analyze','forecast','anomalies']:
        s=sub.add_parser(name); s.add_argument('path'); s.add_argument('--days',type=int,default=30)
    args=p.parse_args(); df=load(args.path)
    if args.cmd=='analyze':
        t,teams,services=analyze(df); print(f'Total: ${t:,.2f}\n\nTeams:\n{teams}\n\nServices:\n{services}')
    elif args.cmd=='forecast': print(f'Forecast ({args.days} days): ${forecast(df,args.days):,.2f}')
    else: print(anomalies(df).to_string() if len(anomalies(df)) else 'No anomalies detected')
if __name__=='__main__': main()
