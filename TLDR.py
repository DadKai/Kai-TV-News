import feedparser
from gtts import gTTS
from datetime import datetime
import os
import re

# Use a reliable RSS feed
FEED_URL = "https://techcrunch.com/feed/"

feed = feedparser.parse(FEED_URL)

if len(feed.entries) == 0:
    print("No articles found.")
    exit()

text_parts = ["Welcome to today's Tech News briefing."]

for entry in feed.entries[:5]:  # first 5 stories
    title = entry.get("title", "")
    description = entry.get("summary", entry.get("description", ""))
    
    # Clean HTML tags
    description = re.sub('<.*?>', '', description)
    
    # Add a clear pause/indicator between stories
    text_parts.append(f"Title: {title}. Article: {description}.")

full_text = " ".join(text_parts)

# Save in Documents folder
filename = f"tech-news-{datetime.now().strftime('%Y-%m-%d')}.mp3"


tts = gTTS(text=full_text, lang="en")
tts.save(filename)

print("Generated:", filename)
