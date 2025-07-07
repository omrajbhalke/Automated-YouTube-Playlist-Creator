# pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube"]

def get_song_names_from_folder(folder_path):
    valid_extensions = ('.mp3', '.wav', '.m4a')
    song_names = [
        os.path.splitext(file)[0]
        for file in os.listdir(folder_path)
        if file.endswith(valid_extensions)
    ]
    return song_names

def search_youtube_video_id(api_key, query):
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            maxResults=1
        )
        response = request.execute()
        items = response.get('items', [])
        if items:
            return items[0]['id']['videoId']
        else:
            return None
    except Exception as e:
        print(f"Error searching for '{query}': {e}")
        return None

def authenticate_youtube_oauth():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES) #change file name to credentials.json
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)

def create_youtube_playlist(youtube, title="My Songs Playlist", description="Auto-created playlist"):
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response = request.execute()
    print(f"✅ Playlist created: {response['snippet']['title']}")
    return response["id"]

def add_video_to_playlist(youtube, playlist_id, video_id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    response = request.execute()
    print(f"🎵 Added: https://youtu.be/{video_id}")

if __name__ == "__main__":
    api_key = input("🔑 Enter your YouTube Data API Key: ").strip()
    folder_path = input("📁 Enter the full path to your music folder: ").strip()
    playlist_title = input("🎧 Enter a name for your new YouTube playlist: ").strip()

    print("\n📂 Reading songs from folder...")
    songs = get_song_names_from_folder(folder_path)
    print(f"🎶 Found {len(songs)} songs:\n")

    video_ids = []
    for song in songs:
        print(f"🔍 Searching YouTube for: {song}")
        video_id = search_youtube_video_id(api_key, song)
        if video_id:
            video_ids.append(video_id)
            print(f"✅ Found: https://www.youtube.com/watch?v={video_id}\n")
        else:
            print(f"❌ Not found: {song}\n")

    print("🔐 Authenticating with YouTube...")
    youtube = authenticate_youtube_oauth()

    playlist_id = create_youtube_playlist(youtube, title=playlist_title)

    print("📥 Adding videos to playlist...")
    for vid in video_ids:
        add_video_to_playlist(youtube, playlist_id, vid)

    print("\n🎉 Done! Your playlist has been created and populated.")
