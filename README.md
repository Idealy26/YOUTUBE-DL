# 🎬 YouTube Video/Audio Downloader

Un script Python simple et rapide pour télécharger des vidéos ou de l'audio depuis YouTube à l'aide de la bibliothèque puissante [`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

---

## ✨ Fonctionnalités

- 📥 Téléchargement de vidéos en haute qualité au format MP4
- 🎵 Extraction d'audio en MP3 (qualité 192 kbps)
- 🖥️ Interface simple via le terminal (choix entre vidéo ou audio)
- ⚡ Téléchargement accéléré avec connexions parallèles (`concurrent_fragment_downloads`)
- 📁 Sauvegarde automatique dans un dossier `downloads/`

---

## ⚙️ Installation

### ✅ Prérequis

- Python 3.6 ou supérieur
- [`ffmpeg`](https://ffmpeg.org/) (obligatoire pour l'extraction audio)
- Accès à la ligne de commande

### 🧪 Étapes

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Idealy26/YOUTUBE-DL
   cd YOUTUBE-DL

2. Installez les dépendances Python :

pip install -r requirements.txt

3. Installez ffmpeg si ce n'est pas déjà fait :

Linux : sudo apt install ffmpeg

macOS : brew install ffmpeg

Windows : Télécharger ici "https://www.ffmpeg.org/download.html" et ajouter ffmpeg.exe au PATH

▶️ Utilisation
Exécutez le script :

python youtube.py
Saisissez les informations demandées :

🔗 Lien de la vidéo YouTube

📌 Type de téléchargement : video ou mp3

Les fichiers seront enregistrés dans le dossier downloads/.