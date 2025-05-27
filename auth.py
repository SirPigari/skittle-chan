from flask import Flask, redirect, url_for, session
from flask_discord import DiscordOAuth2Session
import json

app = Flask(__name__)

# 🔐 Secret Key (Keep this safe!)
app.secret_key = "your_secret_key_here"

# 🔑 Discord OAuth2 Credentials
app.config["DISCORD_CLIENT_ID"] = "YOUR_BOT_CLIENT_ID"
app.config["DISCORD_CLIENT_SECRET"] = "YOUR_BOT_CLIENT_SECRET"
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"
app.config["DISCORD_BOT_TOKEN"] = "YOUR_BOT_TOKEN"

discord = DiscordOAuth2Session(app)

# ✅ Storage for Authorized Users
AUTHORIZED_USERS_FILE = "json/authorized_users.json"

def load_authorized_users():
    try:
        with open(AUTHORIZED_USERS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_authorized_users(users):
    with open(AUTHORIZED_USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# 📌 Homepage (Login Page)
@app.route("/")
def home():
    return redirect(url_for("login"))

# 🔑 OAuth2 Login
@app.route("/login")
def login():
    return discord.create_session(scope=["identify", "connections"])

# 🔄 OAuth2 Callback (After User Logs In)
@app.route("/callback")
def callback():
    discord.callback()
    user = discord.fetch_user()

    # 📌 Load current authorized users
    authorized_users = load_authorized_users()
    authorized_users[str(user.id)] = {
        "username": user.name,
        "discriminator": user.discriminator,
        "avatar": str(user.avatar_url),
    }

    # ✅ Save updated user list
    save_authorized_users(authorized_users)

    return f"✅ Successfully authorized {user.name}#{user.discriminator}! You can close this page."

# 🚪 Logout
@app.route("/logout")
def logout():
    discord.revoke()
    return redirect(url_for("home"))

# 🔥 Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
