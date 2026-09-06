import argparse
import numpy as np
import pandas as pd


def load(path):
    df = pd.read_csv(path, parse_dates=["date"])
    df["cost_usd"] = df["cost_usd"].astype(float)
    return df


def analyze(df):
    total = df.cost_usd.sum()
    by_team = df.groupby("team").cost_usd.sum().sort_values(ascending=False)
    by_service = df.groupby("service").cost_usd.sum().sort_values(ascending=False)
    return total, by_team, by_service


def forecast(df, days=30):
    daily = df.groupby("date").cost_usd.sum().sort_index()
    if len(daily) < 2:
        return float(daily.iloc[-1]) if len(daily) else 0

    x = np.arange(len(daily))
    slope, intercept = np.polyfit(x, daily.values, 1)
    future = np.arange(len(daily), len(daily) + days)
    return max(0, float(np.maximum(0, slope * future + intercept).sum()))


def anomalies(df, threshold=3.5):
    """Detect unusually high daily spend using a robust MAD-based score."""
    daily = df.groupby("date").cost_usd.sum().sort_index()
    if daily.empty:
        return daily

    median = daily.median()
    absolute_deviation = (daily - median).abs()
    mad = absolute_deviation.median()

    if mad == 0:
        return daily[daily > median]

    modified_z = 0.6745 * (daily - median) / mad
    return daily[modified_z > threshold]


def report(df):
    total, teams, services = analyze(df)
    lines = [
        "# FinOps Demo Report",
        "",
        f"**Total spend:** ${total:,.2f}",
        "",
        "## Spend by team",
        "",
    ]
    lines += [f"- {k}: ${v:,.2f}" for k, v in teams.items()]
    lines += ["", "## Spend by service", ""]
    lines += [f"- {k}: ${v:,.2f}" for k, v in services.items()]
    lines += [
        "",
        "## Forecast",
        "",
        f"- Estimated next 30 days: ${forecast(df):,.2f}",
        "",
        "## Anomalies",
        "",
    ]
    hits = anomalies(df)
    lines += [f"- {d.date()}: ${v:,.2f}" for d, v in hits.items()] or ["- None detected"]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    for name in ["analyze", "forecast", "anomalies"]:
        command = sub.add_parser(name)
        command.add_argument("path")
        command.add_argument("--days", type=int, default=30)

    args = parser.parse_args()
    df = load(args.path)

    if args.cmd == "analyze":
        total, teams, services = analyze(df)
        print(f"Total: ${total:,.2f}\n\nTeams:\n{teams}\n\nServices:\n{services}")
    elif args.cmd == "forecast":
        print(f"Forecast ({args.days} days): ${forecast(df, args.days):,.2f}")
    else:
        hits = anomalies(df)
        print(hits.to_string() if len(hits) else "No anomalies detected")


if __name__ == "__main__":
    main()
