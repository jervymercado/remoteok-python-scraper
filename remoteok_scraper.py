# Import the 'requests' library to make HTTP requests (used to fetch data from APIs/websites)
import requests
# Import pandas (as pd) for working with tables and CSV files
import pandas as pd

# URL for the RemoteOK API
url = "https://remoteok.com/api"

# Add headers so the request looks like it's coming from a browser
headers = {"User-Agent": "Mozilla/5.0"}

# Send a GET request to the API
response = requests.get(url, headers=headers)

# Convert response to JSON and skip the first element (it's just metadata)
jobs = response.json()[1:]

python_jobs = []  # list to hold only Python-related jobs

# Loop through all jobs
for job in jobs:
    # Normalize tags to lowercase to make matching easier
    tags = [tag.lower() for tag in job.get("tags", [])]

    # If "python" appears in the job tags, save it
    if "python" in tags:
        python_jobs.append({
            "title": job.get("position"),                     # job title
            "company": job.get("company"),                    # company name
            "link": "https://remoteok.com" + job.get("url")   # full job link
        })

# Convert Python job list into a DataFrame
df = pd.DataFrame(python_jobs)

# Save DataFrame to CSV file
df.to_csv("remoteok_python_jobs.csv", index=False)

# Print first 5 rows of results (for preview)
print(df.head())

# Print how many jobs were saved
print(f"Saved {len(df)} jobs to CSV")
