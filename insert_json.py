# pyAirtable docs
# https://pyairtable.readthedocs.io/en/stable/getting-started.html
# Airtable API
# https://airtable.com/developers/web/api/introduction
# NICAR 2024 JSON
# https://schedules.ire.org/nicar-2024/nicar-2024-schedule.json

# A keeper:
# "session_id": 2119,
# "session_title": "Using AI tools for data journalism",
# Also, chris amico, simon willison & derek willis



from pyairtable import Table
import json

# Load your JSON data
with open('your_data.json') as f:
    data = json.load(f)

# Connect to your Airtable base
table = Table('Your API Key', 'Your Base ID', 'Your Table Name')

# Iterate over your JSON data and insert each record
for record in data:
    table.insert(record)
