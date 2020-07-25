import subprocess
command = 'for file in *.mp4; do ffmpeg -i "$file" -c copy -an "measure_$file"; done'
subprocess.call(command, shell=True)