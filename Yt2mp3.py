from yt_dlp import YoutubeDL


(option,C1,C2,C3) = [dict(format="bestaudio/best",extracaudio=True),"https://youtu.be","https://www.youtube.com","https://youtube.com"]


def download(link):
    if not (C1 in link or C2 in link or C3 in link):
        quit("[!] Invalid Video Url\n")

    with YoutubeDL(option) as YTA:
        YTA.download([link])
    
    return True


if __name__ == '__main__':
    
    url = input("Enter Your Video Url: ")
    if download(url):
        print("\n[+] Video Downloaded...\n")