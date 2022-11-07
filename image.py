import praw, os, subprocess, time, requests, re, json, _thread
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

g_data=[]
for i in range(4,1580):
    image_no=0
    jso=json.load(open(f"Chodi/{str(i)}chodi.json"))
    print(i)
    for data in jso['data']:
        if "i.redd.it" in data['url']:
            req=requests.get(data['url'])
            #req=200
            if req.status_code==200:
                image_no+=1
                print(f"{data['url']}")
                with open(f"images/{str(i)}_{str(image_no)}_image.jpg", "wb") as file:
                    file.write(req.content)
                if len(data['title'])<180:
                    g_data.append({"image_path": f"images/{str(i)}_{str(image_no)}_image.jpg", "caption": f"{data['title']}"})
                else:
                    g_data.append({"image_path": f"images/{str(i)}_{str(image_no)}_image.jpg"})
                if len(g_data)>15:
                    title=f"__{str(i)}__ images:15"
                    _thread.start_new_thread(post_gallery, (title, g_data,i,0))
                    g_data=[]

while True:
    pass
