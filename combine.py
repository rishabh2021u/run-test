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

subreddit=reddit.subreddit('u_OkAppearance1201')

subreddit=reddit.subreddit('ChodiUniverse')
done=open("done.txt").read().splitlines()

def post_video(title,path,sleep):
    time.sleep(sleep)
    try:
        wat=path.replace(".mp4", "")+ "_watthumb.png"
        subprocess.call(['ffmpeg', '-i', f'{path}', '-ss', '00:00:01.000', '-vframes','1', f'{wat}', '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        submission=subreddit.submit_video(title, path, thumbnail_path=wat)
        print(submission.permalink)
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
    os.system(f"yt-dlp {data['url']}/DASHPlaylist.mpd -o videos/{file_name}")
    # os.system(f"youtube-dl {data['url']}/DASHPlaylist.mpd -o videos/{file_name}")
    if os.path.exists(f"videos/{file_name}"):
        print(f"{data['url']}")
        title=data['title']
        # post_video(title,f"videos/{file_name}",0)
        with open(f"done.txt", "a") as file:
            file.write(data['url']+"\n")
        _thread.start_new_thread(post_video, (title, f"videos/{file_name}",0))

def image(data, sleep):
    filename=f"{str(uuid.uuid1())}.jpg"
    time.sleep(sleep)
    req=requests.get(data['url'])
    if req.status_code==200:
        print(f"{data['url']}")
        with open(f"images/{filename}", "wb") as file:
            file.write(req.content)
        submission=subreddit.submit_image(data['title'], f"images/{filename}")
        os.remove(f"images/{filename}")
        print(submission.permalink)
    with open(f"done.txt", "a") as file:
        file.write(data['url']+"\n")


g_data=[]
th=0
vi=0
im=0
for i in range(4,5):
    image_no=0
    jso=json.load(open(f"Chodi/{str(i)}chodi.json"))
    print(i)
    for data in jso['data']:
        if data['url'] not in done:
            if "i.redd.it" in data['url'] and im < 11:
                im+=1
                _thread.start_new_thread(image, (data,0))
            if "v.redd.it" in data['url']:
                vi+=1
                _thread.start_new_thread(vid, (data, f"videos/{str(vi)}_video.mp4",0))
                if th<4:
                    th+=1
                else:
                    time.sleep(10)
                    th=0

while True:
    pass
