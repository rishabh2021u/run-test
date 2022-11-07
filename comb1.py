import praw, os, subprocess, time, requests, re, json, _thread,uuid
from praw.models import InlineGif, InlineImage, InlineVideo
# import sys
# sys.path.insert(1, '/home/ubuntu/mum/IC')
# import gyfcat
# reddit1 = praw.Reddit(user_name='PdfFileOpener',refresh_token='2252389277312-ZCXJtfseArkexvPu2W0O7mfD4RVONw',client_id='U6nHuczXwm8okuLbFcs4Eg',client_secret='REHGpEGObR5C_sA_J-d8KQodKZNb8Q',redirect_uri='http://localhost:8080',user_agent='testscript by wwu/fakebot3',)
# reddit = praw.Reddit(user_name='Small_Ad484',refresh_token='2338757205073-kLQuJPoM6TcAFCvZt9qbzG9-BjacYw',client_id='U6nHuczXwm8okuLbFcs4Eg',client_secret='REHGpEGObR5C_sA_J-d8KQodKZNb8Q',redirect_uri='http://localhost:8080',user_agent='testscript by u/fakebot3',)
reddit = praw.Reddit(
    client_id="BsAUR5b3R5eyMOyWEUyMoA",
    client_secret="MFk1EnePz92KK8SfZmG7pqZRuS3uSA",
    password="OkAppearance1",
    user_agent="OkAppearance1201:praw (By u/OkAppearance1201)",
    username="OkAppearance1201",
)

# reddit = praw.Reddit(
#     client_id="kwChlrj_VwZZruGYoPvt4A",
#     client_secret="X0kIi6eNwl7eSv01lRPLg1ZptTZ41A",
#     password="Sanatan_sevak",
#     user_agent="Sanatan_sevak20:prawbot (By u/Sanatan_sevak20)",
#     username="Sanatan_sevak20",
# )


subreddit=reddit.subreddit('ChodiUniverse')
done=open("done.txt").read().splitlines()

def post_video(title,path,data,sleep):
    time.sleep(sleep)
    try:
        wat=path.replace(".mp4", "")+ "_watthumb.png"
        subprocess.call(['ffmpeg', '-i', f'{path}', '-ss', '00:00:01.000', '-vframes','1', f'{wat}', '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        submission=subreddit.submit_video(title, path, thumbnail_path=wat)
        print(f"{submission.permalink} : {submission.title}")
        with open(f"done.txt", "a") as file:
            file.write(data['url']+"\n")
        os.remove(f"{path}")
        os.remove(f"{wat}")
    except Exception as e:
        print(e)
        time.sleep(2)
        post_video(title,path,sleep)

def post_gallery(title,g_data, i,sleep):
    time.sleep(sleep)
    try:
        submission=subreddit.submit_gallery(title, g_data)
        print(submission.permalink)
        for it in g_data:
            os.remove(f"{it['image_path']}")
    except Exception as e:
        print(e)
        time.sleep(2)
        post_gallery(title,g_data, i,sleep)

def vid(data, file_name,sleep):
    video_url=f"{data['url']}/DASH_720.mp4"
    video_url480=f"{data['url']}/DASH_480.mp4"
    video_url360=f"{data['url']}/DASH_360.mp4"
    video_url240=f"{data['url']}/DASH_240.mp4"
    audio_url=f"{data['url']}/DASH_audio.mp4"
    headers = {'User-Agent':'Mozilla/5.0'}
    with open(f'/tmp/{file_name}_video.mp4','wb') as file:
        response = requests.get(video_url,headers=headers)
        if(response.status_code == 200):
            file.write(response.content)
        else:
            response = requests.get(video_url480,headers=headers)
            if(response.status_code == 200):
                file.write(response.content)
            else:
                response = requests.get(video_url360,headers=headers)
                if(response.status_code == 200):
                    file.write(response.content)
                else:
                    response = requests.get(video_url240,headers=headers)
                    if(response.status_code == 200):
                        file.write(response.content)
                    else:
                        print(f"no video found for {data['url']}")
    with open(f'/tmp/{file_name}_audio.mp3','wb') as file:
        print('Downloading Audio...',end = '',flush = True)
        response = requests.get(audio_url,headers=headers)
        if(response.status_code == 200):
            file.write(response.content)
            print('\rAudio Downloaded...!')
        else:
            print(f"\rAudio Download Failed..! for {data['url']}")
    if os.path.exists(f'/tmp/{file_name}_video.mp4')==True and os.path.exists(f'/tmp/{file_name}_audio.mp3')==True:
        subprocess.call(['ffmpeg','-i',f'/tmp/{file_name}_video.mp4','-i',f'/tmp/{file_name}_audio.mp3','-map','0:v','-map','1:a','-c:v','copy',f'/tmp/{file_name}.mp4', '-y'],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT) #, ' > /dev/null 2> /dev/null'
    elif os.path.exists(f'/tmp/{file_name}_video.mp4')==True and os.path.exists(f'/tmp/{file_name}_audio.mp3')!=True:
        os.system(f"cp /tmp/{file_name}_video.mp4 /tmp/{file_name}.mp4")
    else:
        os.system(f"yt-dlp {data['url']}/DASHPlaylist.mpd -o /tmp/{file_name}.mp4")
        if os.path.exists(f'/tmp/{file_name}.mp4')!=True:
            os.system(f"yt-dlp  {data['url']}/HLSPlaylist.m3u8 -o /tmp/{file_name}.mp4")
    subprocess.call(['rm',f'/tmp/{file_name}_video.mp4',f'/tmp/{file_name}_audio.mp3'])
    # os.system(f"yt-dlp {data['url']}/DASHPlaylist.mpd -o /tmp/{file_name}.mp4")
    # if os.path.exists(f'/tmp/{file_name}.mp4') !=True:
    #     os.system(f"yt-dlp  {data['url']}/HLSPlaylist.m3u8 -o /tmp/{file_name}.mp4")
    # os.system(f"youtube-dl {data['url']}/DASHPlaylist.mpd -o videos/{file_name}")
    if os.path.exists(f'/tmp/{file_name}.mp4'):
        print(f"{data['title']} : {data['url']}")
        title=data['title']
        # post_video(title,f"videos/{file_name}",0)
        _thread.start_new_thread(post_video, (title, f'/tmp/{file_name}.mp4',data,0))

def image(data, sleep):
    filename=f"{str(uuid.uuid1())}.jpg"
    time.sleep(sleep)
    req=requests.get(data['url'])
    if req.status_code==200:
        print(f"{data['title']} : {data['url']}")
        with open(f"/tmp/{filename}", "wb") as file:
            file.write(req.content)
        submission=subreddit.submit_image(data['title'], f"/tmp/{filename}")
        os.remove(f"/tmp/{filename}")
        print(f"{submission.permalink} : {submission.title}")
    with open(f"done.txt", "a") as file:
        file.write(data['url']+"\n")


g_data=[]
th=0
vi=0
im=0
for i in range(13,23):
    image_no=0
    jso=json.load(open(f"/Chodi/{str(i)}chodi.json"))
    print(i)
    for data in jso['data']:
        if data['url'] not in done:
            if "i.redd.it" in data['url']:
                im+=1
                _thread.start_new_thread(image, (data,0))
            if "v.redd.it" in data['url']:
                vi+=1
                print(data['url'])
                _thread.start_new_thread(vid, (data, f"{str(vi)}_video",0))
                if th<3:
                    th+=1
                else:
                    time.sleep(30)
                    th=0

while True:
    time.sleep(5)
    print(".")
    pass
