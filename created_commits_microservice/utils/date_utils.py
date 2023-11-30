from datetime import datetime, timedelta

current_date = datetime.now()
first_day_of_month = current_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
last_day_of_month = (current_date.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)

last_date = ((datetime.utcnow()-timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)).strftime("%Y-%m-%dT%H:%M:%SZ")