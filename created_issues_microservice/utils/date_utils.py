from datetime import datetime, timedelta

last_date = ((datetime.utcnow()-timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)).strftime("%Y-%m-%dT%H:%M:%SZ")