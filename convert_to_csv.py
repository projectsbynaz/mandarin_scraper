import json
import csv

# Load phrases
with open('phrases.json', 'r', encoding='utf-8') as f:
    phrases = json.load(f)

# Load topics
with open('topics.json', 'r', encoding='utf-8') as f:
    topics = json.load(f)

# Create a mapping from topic name to URL
topic_url_map = {topic['topic']: topic['url'] for topic in topics}

# Prepare rows for CSV
rows = []
for phrase in phrases:
    topic_raw = phrase['topic']
    # Remove numeric prefix (e.g. "01 - Greetings" → "Greetings")
    topic_clean = topic_raw.split(' - ', 1)[1] if ' - ' in topic_raw else topic_raw
    english = phrase['english']
    mandarin = phrase['chinese']
    # Replace non-breaking spaces in Pinyin
    pinyin = phrase['pinyin'].replace('\xa0', ' ')
    url = topic_url_map.get(topic_raw, '')

    rows.append([topic_clean, english, mandarin, pinyin, url])

# Write to CSV
with open('phrases_cleaned.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Topic', 'English', 'Mandarin', 'Pinyin', 'URL'])
    writer.writerows(rows)

print("CSV file 'phrases_cleaned.csv' created successfully")
