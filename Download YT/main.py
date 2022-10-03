from pytube import YouTube, streams

url = input(str(' Insira a url do video: '))
video = YouTube(url)
baixarvideo = video.streams.get_highest_resolution()
baixarvideo.download()

print('Download concluido com sucesso!!')
