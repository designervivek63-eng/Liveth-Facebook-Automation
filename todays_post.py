"""Reads data/content-plan.csv and writes today's post brief to post_brief.md.
Sets GitHub Actions output has_post=true only on 'Post' days (alternate days)."""
import csv, json, os
from datetime import datetime, timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))
today = datetime.now(IST).date()
start = datetime.strptime(json.load(open("data/config.json"))["start_date"], "%Y-%m-%d").date()
day = (today - start).days + 1

def out(k, v):
    p = os.environ.get("GITHUB_OUTPUT")
    if p:
        with open(p, "a") as f: f.write(f"{k}={v}\n")
    print(f"{k}={v}")

row = None
if 1 <= day <= 15:
    for r in csv.DictReader(open("data/content-plan.csv", encoding="utf-8")):
        if int(r["day"]) == day: row = r

if row and row["status"] == "Post":
    body = f"""# Day {day} - {row['pillar']}: {row['topic']}

**Date:** {today}

**Static image concept:** {row['image_concept']}

**Headline on creative:** {row['headline']}

**Caption hook:** {row['caption_hook']}

**CTA:** {row['cta']}

**Hashtags:** {row['hashtags']}

**Size:** 1080x1350 (4:5)
"""
    open("post_brief.md", "w", encoding="utf-8").write(body)
    out("has_post", "true"); out("title", f"Day {day}: {row['topic']}")
else:
    out("has_post", "false")
