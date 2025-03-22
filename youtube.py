import yt_dlp

def download_video(url, output_path="downloads", mode="video"):
    try:
        if mode == "video":
            ydl_opts = {
                'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',  # Meilleure vidéo + audio
                'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                'merge_output_format': 'mp4',  # Fusionner en MP4 si séparé
            }
            print("🎥 Téléchargement de la vidéo en MP4...")
        elif mode == "audio":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            print("🎵 Téléchargement de l'audio en MP3...")

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