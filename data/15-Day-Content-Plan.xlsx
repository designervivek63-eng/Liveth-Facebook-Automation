# 15-Day Content Plan Automation (@vivek.branding)

Static image plan for branding and marketing posts. Posts go out every other day (Days 1, 3, 5 ... 15).

## Files
- `data/15-Day-Content-Plan.xlsx` - the full plan sheet (edit start date in cell C2)
- `data/content-plan.csv` - same plan in CSV, read by the automation
- `data/config.json` - `start_date` (YYYY-MM-DD). Keep it in sync with the sheet
- `scripts/todays_post.py` - picks today's post (IST) and writes `post_brief.md`
- `.github/workflows/daily-content-reminder.yml` - runs daily at 9:00 AM IST and opens a GitHub issue with that day's post brief on post days

## Setup
1. Create a GitHub repo and upload everything in this folder (keep the `.github/workflows/` path exactly).
2. Check **Settings -> Actions -> General -> Workflow permissions** allows read and write.
3. Change `start_date` in `data/config.json` if needed.
4. Test it: **Actions -> Daily content reminder -> Run workflow**. An issue appears only if today is a post day within the 15 days.

No secrets or API keys are needed.
