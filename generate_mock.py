import random
import json

# Generate mock data
data = []
for i in range(10):
    name = f"Name {i}"
    title = f"Title {i}"
    subtitle = f"Subtitle {i}"
    created_at = f"{random.randint(2000, 2022)}-{'{:02d}'.format(random.randint(1, 12))}-{'{:02d}'.format(random.randint(1, 28))}T{'{:02d}'.format(random.randint(0, 23))}:{'{:02d}'.format(random.randint(0, 59))}:{'{:02d}'.format(random.randint(0, 59))}Z"
    data.append({
        'name': name,
        'title': title,
        'subtitle': subtitle,
        'created_at': created_at
    })

# Write the data to a file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
