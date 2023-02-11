ffmpeg -i media/videos/main/1080p60/DefaultTemplate.mp4 -i introduction.mp3 -map 0:v -map 1:a -c:v copy -shortest output.mp4
