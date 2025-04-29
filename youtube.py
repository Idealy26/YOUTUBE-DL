import yt_dlp
import os

def download_video(url, output_path="downloads", mode="video"):
    try:
        os.makedirs(output_path, exist_ok=True)

        # Options communes
        base_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'noplaylist': True,  # Ne pas télécharger les playlists complètes
            'quiet': False,
            'concurrent_fragment_downloads': 4,  # Téléchargement multi-threads
            'retries': 3,
            'fragment_retries': 3,
            'no_warnings': True,
        }

        if mode == "video":
            print("🎥 Téléchargement rapide de la vidéo en MP4...")
            ydl_opts = {
                **base_opts,
                'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
                'merge_output_format': 'mp4',
            }
        elif mode == "audio":
            print("🎵 Téléchargement rapide de l'audio en MP3...")
            ydl_opts = {
                **base_opts,
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        else:
            raise ValueError("Mode invalide")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("✅ Téléchargement terminé !")

    except Exception as e:
        print(f"❌ Erreur : {e}")

# Demander à l'utilisateur son choix
url = input("🔗 Entrez l'URL YouTube : ")
mode = input("📌 Voulez-vous télécharger en (video/mp3) ? ").strip().lower()

if mode not in ["video", "mp3"]:
    print("❌ Choix invalide ! Par défaut, téléchargement en vidéo.")
    mode = "video"

download_video(url, mode="audio" if mode == "mp3" else "video")