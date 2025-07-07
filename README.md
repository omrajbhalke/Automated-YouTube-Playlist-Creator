# 🎵 Automated YouTube Playlist Creator

A Python-based tool that automates the process of creating a YouTube playlist using song titles from your local music folder. It uses the YouTube Data API to search songs and add them to a new playlist on your YouTube account.

---

## 📌 Features

* ✅ Automatically reads song names from a local folder.
* 🔍 Searches each song on YouTube.
* 🎥 Adds top matching videos to a newly created playlist on your YouTube account.
* 📂 Supports `.mp3`, `.wav`, and other audio file extensions.
* 💡 Optionally filters out duplicates or undesired results.
* 🔒 Uses OAuth 2.0 to authorize secure access to your YouTube account.

---

## 📁 Project Structure

```
automated-youtube-playlist-creator/
│
├── credentials.json         # OAuth client credentials from Google Cloud Console
├── playlist_creator.py      # Main script to run the tool
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── songs/                   # Folder containing your local music files
```

---

## 🔧 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/automated-youtube-playlist-creator.git
cd automated-youtube-playlist-creator
```

2. **Set up Virtual Environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install Required Libraries**

```bash
pip install -r requirements.txt
```

---

## 🔐 Google API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the **YouTube Data API v3** for the project.
4. Go to **Credentials** → **Create OAuth client ID** → Choose **Desktop App**.
5. Download the `credentials.json` file and replace it in the project root directory.
6. For more detailed explanation check out [steps.docx](steps.docx)
---

## ▶️ How to Use

1. Place your songs in the `songs/` directory. Make sure file names include artist and song name (e.g., `Imagine Dragons - Believer.mp3`).
2. Run the script:

```bash
python playlist_creator.py
```

3. When prompted:

   * Log in via the Google account you want to create the playlist with.
   * Grant permission to access YouTube account.
   * Enter a name for the playlist when prompted.

The script will:

* Read song names from your `songs/` folder.
* Search YouTube for each song.
* Create a new YouTube playlist.
* Add the top search result of each song to that playlist.

---

## ⚙️ Configuration Options (Optional)

You can customize the script by editing `playlist_creator.py`:

* Set playlist privacy: `public`, `private`, or `unlisted`
* Adjust max number of videos to add
* Apply keyword filters for search optimization

---

## 🧪 Example

```bash
$ python playlist_creator.py

Enter a name for the new YouTube playlist: My Workout Mix
Created playlist: My Workout Mix (ID: PLxxxxxxxxxxxxxxxx)

Searching for: Imagine Dragons - Believer
Added: Believer - Imagine Dragons (Official Music Video)

Searching for: Ed Sheeran - Shape of You
Added: Ed Sheeran - Shape of You (Official Video)

...
```

---

## ✅ Requirements

* Python 3.7+
* YouTube Data API enabled and `credentials.json` file
* Internet connection

---

## 📦 Dependencies

```
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
```

Install via:

```bash
pip install -r requirements.txt
```

---

## ❗ Known Limitations

* Accuracy depends on YouTube search results and song title format.
* Only first search result is added—may not always be the exact match.
* API quota limits may apply (\~10,000 units/day).
* Doesn't verify if videos are official or duplicates.

---

## 🚀 Future Enhancements

* GUI or web-based interface.
* More accurate matching using artist/album metadata.
* Add retry mechanism for failed searches.
* Option to review or skip songs manually.
* Smart duplicate detection or cross-check with playlist contents.

---

## 🧑‍💻 Author

* **Omraj Bhalke** – [GitHub](https://github.com/omrajbhalke)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
