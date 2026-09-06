import pandas as pd
from finops.analytics import analyze, forecast, anomalies

def test_analyze():
    df=pd.DataFrame({'date':pd.to_datetime(['2026-01-01','2026-01-02']),'team':['platform','app'],'service':['EC2','RDS'],'cost_usd':[10,20]})
    total,teams,services=analyze(df)
    assert total==30 and teams['app']==20

def test_forecast_non_negative():
    df=pd.DataFrame({'date':pd.date_range('2026-01-01',periods=5),'cost_usd':[10,11,12,13,14]})
    assert forecast(df,7)>=0

def test_anomalies():
    df=pd.DataFrame({'date':pd.date_range('2026-01-01',periods=5),'cost_usd':[10,10,10,10,100]})
    assert len(anomalies(df))==1
