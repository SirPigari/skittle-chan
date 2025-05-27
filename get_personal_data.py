import json
import os
import zipfile

# Inputs for user information
user_id = input("USER ID: ")
username = input("USER NAME: ")

# Load the JSON data
with open("json/conversation_histories.json") as f:
    conversation_histories = json.load(f)
conversation_history = conversation_histories.get(username, {})

with open("json/logged_users.json") as f:
    logged_users = json.load(f)
logged_user = logged_users.get(user_id, {})

with open("json/command_logs.json") as f:
    command_logs_ = json.load(f)
command_logs = [i for i in command_logs_ if i["user_id"] == int(user_id)]

# Load message log and filter messages sent by or involving the user
with open("json/message_logs.json") as f:
    message_logs = json.load(f)

user_messages = {}
for channel_id, messages in message_logs.items():
    relevant_messages = [
        msg for msg in messages
        if f"-{user_id}]" in msg or f"(DM with {username})" in msg
    ]
    if relevant_messages:
        user_messages[channel_id] = relevant_messages

# Create a directory for temporary files
output_dir = "temp_json"
os.makedirs(output_dir, exist_ok=True)

# Save each dictionary to a JSON file
files_to_zip = {
    "conversation_history.json": conversation_history,
    "logged_user.json": logged_user,
    "command_logs.json": command_logs,
    "user_messages.json": user_messages,
}

for filename, data in files_to_zip.items():
    with open(os.path.join(output_dir, filename), "w") as f:
        json.dump(data, f, indent=4)

# Create a zip file containing the JSON files
zip_filename = f"{username}-{user_id}.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for filename in files_to_zip.keys():
        zipf.write(os.path.join(output_dir, filename), filename)

# Clean up the temporary files
for filename in files_to_zip.keys():
    os.remove(os.path.join(output_dir, filename))
os.rmdir(output_dir)

print(f"Zip file '{zip_filename}' created successfully!")
