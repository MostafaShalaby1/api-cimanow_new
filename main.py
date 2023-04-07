# from urllib.parse import urlparse, quote

# url = "https://ar.cimanow.online/مسلسل-جعفر-العمدة-الحلقة-10-العاشرة/watching/"

# # Parse the URL to get the path component
# path = urlparse(url).path

# # Encode the path component using percent-encoding
# encoded_path = quote(path)

# # Construct the new URL with the encoded path component
# new_url = "https://ar.cimanow.online" + encoded_path

# print(new_url)



import requests, json
from flask import Flask
from threading import Thread
from urllib.parse import urlparse, quote
# import socket
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
 
# print("Your Server Name is : " + hostname)
# print("Your Server IP Address is : " + IPAddr)
app = Flask('')

allowed_ips =requests.get("https://pastebin.com/raw/fq5ngNP6").text
if IPAddr in allowed_ips:
    print (" Your Server Can Use This api ")
else:
    exit("Api Can't Run in This Server ,bro\n You Can Call Me in Telegram \t https://t.me/xb7od (@xb7od)")
@app.route('/')
def home():
	return  "I'm alive"
@app.route('/link=<string:name>', methods=['GET'])
def get_name(name):
  BigArry={}
  getlinks=0
  name=name
  name=name.split('<')[1]
  name=name.split('>')[0]
  link=name.replace("+","/")
  if "//getlinks//" in link:
      link=link.replace("//getlinks//","")
      getlinks=1
  
  def req(link):
    link=link

    link=link.replace("https://","")   
    link=link.replace("//","/")
    link="https://"+link
    #print(BigArry)
    hes ={'user-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:32.0) Gecko/20100101 Firefox/32.0'}
    re= requests.get(link, headers=hes)
    return re.text
  def req2(lin,ref):
    lin=lin.replace("https://","")   
    lin=lin.replace("//","/")
    lin="https://"+lin
    ref=ref.replace("https://","")   
    ref=ref.replace("//","/")
    ref="https://"+ref
    path = urlparse(lin).path

    # Encode the path component using percent-encoding
    encoded_path = quote(path)
    lin=lin.replace("https://","")
    lin=lin.split("/")[0]
    # Construct the new URL with the encoded path component
    new_url =lin+"/" + encoded_path
    new_url=new_url.replace("//","/")
    new_url=new_url.replace("//","/")
    new_url=new_url.replace("//","/")
    new_url = "https://"+new_url
    # print(new_url)
    hes ={
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'referer':new_url,
        'user-agent': 'Mozilla/5.0 (Windows NT 5.1; rv:32.0) Gecko/20100101 Firefox/32.0'}
    re= requests.get(ref, headers=hes)
    return re.text
  
  def main(link):   
    
    if "/watching" in link:
        link=link.replace("/watching","")    
    data=req(link)
    #print(data)
    title =data.split('<title>')[1]
    title =title.split('</title>')[0]
    if ' | سيما ناو - Cima Now' in title:
        title =title.split(' | سيما ناو - Cima Now')[0]
    if "الموسم"in title:
        title1=title.split("الموسم")[0]
        try:
            title2=title.split("الحلقة")[1]
        except:    
            title2=title.split("الحلقه")[1]
        title= title1+"الحلقة"+title2     
    BigArry['title']=title
    a=0
    if "فيلم" in title:
        a=1
    if "برنامج" in title:
        a=1    
    if "حلقه" in title:
        a=1
    if "الحلقة" in title:
        a=1
    if "الحلقه" in title:
        a=1            
    if a ==1:
        info =data.split('<ul class="tabcontent" id="details">')[1]
        info =info.split("a></li></ul>")[0]
        try:
            story = data.split("""<meta name="description" content='""")[1]
            story =story.split("' />")[0]
        except:
            story = info.split("</i>لمحة عامة : </strong><p>")[1]
            story =story.split("</p></li>")[0]
        if "&nbsp;" in story:
            story=story.replace("&nbsp;", " ")

        BigArry['story']=story
        photo =data.split('<figure>')[1]
        photo =photo.split('</ul>')[0]
        try:
            logo= photo.split('<img  src="')[1]
            logo= logo.split('" alt="')[0]
            cover1= photo.split('<img  src="')[2]
            cover=cover1.split('" alt="')[0]
        except:    
            logo= photo.split('<img src="')[1]
            logo= logo.split('" alt="')[0]
            cover1= photo.split('<img src="')[2]
            cover=cover1.split('" alt="')[0]

        mm=logo
        logo=cover
        cover=mm
        BigArry['logo']=logo
        BigArry['cover']=cover
        try:
            requ= requests.get(cover.replace("كوفر", "كلين")).reason
            if requ =="OK":
                coverMob=cover.replace("كوفر", "كلين")
                BigArry['coverMob']=coverMob
            else:
                coverMob=logo.replace("لوجو", "كلين")
                coverMob=coverMob.replace("png", "jpg")
                requ= requests.get(coverMob).reason
                if requ =="OK":
                    BigArry['coverMob']=coverMob
            
            poster =cover.split("-كوفر")[0]
            poster=poster+".jpg"
            requ= requests.get(poster).reason
            if requ =="OK":
                BigArry['poster']=poster
            else:
                link1=cover.split("//")[0]
                link2=cover.split("//")[1]
                link2=link2.split("/")[0]
                serch=title.replace(" ","+")
                mix=f'{link1}//{link2}/?s={serch}'
                data= req(mix)
                if '<img class="lazy" src="' in data:
                    poster=data.split('<img class="lazy" src="')[1]
                    poster=poster.split('data-src="')[1]
                    poster=poster.split('"')[0]
                    BigArry['poster']=poster    
        except:
            print("No internet")


        mess=cover1.split('/release-year/')[0]
        cat=mess.split('<li><a>')[1]

        category=cat.split('</a></li>')[0]
        BigArry['category']=category

        if "مدة العرض : " in info:
            runtime =info.split('</i>مدة العرض : </strong><a>')[1]
            runtime= runtime.split('</a><li><strong>')[0]
            BigArry['runtime']=runtime

        genre=cat.split('<li>')[2]
        genre=genre.split('</li>')[0]
        BigArry['genre']=genre

        year=data.split('/release-year/')[1]
        year= year.split('/">')[0]
        BigArry['year']=year
        if 'aria-label="comment"' in data:
            comment=data.split('aria-label="comment"')[1]
            comment=comment.split("<em>")[1]
            comment=comment.split("</em>")[0]
            BigArry['comment']=comment
        if "مسلسل" in title or "برنامج" in title:
            series=title.replace(" ج1","")
            series=series.replace(" ج2","")
            series=series.replace(" ج3","")
            series=series.replace(" ج4","")
            series=series.replace(" ج5","")
            series=series.replace(" ج6","")
            series=series.replace(" ج7","")
            try:
                series= title.split(" الحلقة")[0]
            except:
                try:
                    series= title.split(" حلقة ")[0]
                except:    
                    try:

                        series= title.split(" مسلسل ")[0]
                    except:
                        series=title.split("الشاذلي")[0]
                        series=series+"الشاذلي"

            # series=series.replace("مسلسل ","")
            # series=series.replace("برنامج ","")
            try:
                series=series.split(" الموسم")[0]
            except:    
                series=series
            # series=series.replace(" الموسم الثاني","")
            # series=series.replace(" الموسم الاول","")
            # series=series.replace(" الموسم الثالث","")
            # series=series.replace(" الموسم الرابع","")
            # series=series.replace(" الموسم الخامس","")
            # series=series.replace(" الموسم السادس","")
            # series=series.replace(" الموسم السابع","")
            # series=series.replace(" الموسم الثامن","")
            # series=series.replace(" الموسم التاسع","")
            # series=series.replace(" الموسم العاشر","")
            BigArry['series']=series
            number_en=title.split(" الحلقة ")[1]
            number_en=number_en.split(" ")[0]
            BigArry['number_en']=number_en
            if '"season-title">' in data:
                season =data.split('"season-title">')[1]
                season =season.split('الموسم')[1]
                season="الموسم"+season.split('<')[0]
                BigArry['season']=season
            title2=title.replace("مسلسل ","")
            title2=title.replace("برنامج ","")
            BigArry['title']=title2

        if "الجودة : " in info:
            quality =info.split('</i>الجودة : </strong><a>')[1]
            quality= quality.split('</a></li><li><strong>')[0]
            BigArry['quality']=quality


        if "طاقم العمل : " in info:
            
            actor =info.split('</i>طاقم العمل : </strong>')[1]
            actor= actor.split('</li><li>')[0]
            try:
                actors='،'
                for i in range(6):
                    actorr =actor.split('/">')[i+1]
                    actorr =actorr.split('</a>')[0]
                    actors+=" ، "+actorr
            except:    
                try:
                    actors='،'
                    for i in range(5):
                        actorr =actor.split('/">')[i+1]
                        actorr =actorr.split('</a>')[0]
                        actors+=" ، "+actorr
                except:
                    try:
                        actors='،'
                        for i in range(4):
                            actorr =actor.split('/">')[i+1]
                            actorr =actorr.split('</a>')[0]
                            actors+=" ، "+actorr
                    except:
                        try:
                            actors='،'
                            for i in range(3):
                                actorr =actor.split('/">')[i+1]
                                actorr =actorr.split('</a>')[0]
                                actors+=" ، "+actorr
                        except:
                            try:
                                actors='،'
                                for i in range(2):
                                    actorr =actor.split('/">')[i+1]
                                    actorr =actorr.split('</a>')[0]
                                    actors+=" ، "+actorr
                            except:
                                actorr =actor.split('/">')[1]
                                actorr =actorr.split('</a>')[0]
                                actors=actorr
            actors=actors.replace("، ، ", "")
            actors=actors.replace("<", "")
            actors=actors.replace("/", "")
            actors=actors.replace(">", "")
            actors=actors.replace(" ، ", "++")
            actors=actors.replace("،", "")
            actors=actors.replace("++", " ، ")
            BigArry['actor']=actors

        if "اخراج : " in info:
            director =info.split('</i>اخراج : </strong><a href="')[1]
            director= director.split('/">')[1]
            director= director.split('</a>')[0]
            BigArry['director']=director

        if "تأليف : " in info:    
            escritor =info.split('</i>تأليف : </strong><a href="')[1]
            escritor= escritor.split('/">')[1]
            escritor= escritor.split('</a></li></ul>')[0]
            if "</"in escritor:
                escritor=escritor.replace("</","")
            BigArry['escritor']=escritor

        if '<ul class="tabcontent" id="watch">' in data:
            trailer=data.split('<ul class="tabcontent" id="watch">')[1]
            if '<iframe src=""' in trailer:
                aa=1
            else:    
                trailer=trailer.split('<iframe src="')[1]
                trailer=trailer.split('" scrolling=')[0]
                BigArry['trailer']=trailer

  if "الاحدث" in link:
    data = req(link)
    links =data.split('<section aria-label="posts">')[1]
    links =links.split('</section>')[0]
    for i in range(30):
        linkk =links.split('<article aria-label="post">')[30-i]
        linkk=linkk.split('<a href="')[1]
        linkk=linkk.split('"')[0]
        #print(linkk)
        BigArry[f'link{i+1}']=linkk
  
  else:
        
    main(link)
    if getlinks==1:
        
        lin=link+"/watching/"
        domine=lin.replace("https://","")
        domine=domine.split('/')[0]
        domine="https://"+domine+"/"
        data_w=req(lin)
        watchlink = data_w.split('id="watch">')[1]
        theme=data_w.split("/themes/")[1]
        theme=theme.split("/")[0]
        ved_id=watchlink.split('data-id="')[1]
        ved_id=ved_id.split('"')[0]
        watchlink = watchlink.split('</ul>')[0]
        # i=0
        assessment_links = []
        for i in range(7):
            try:
                # i+=1
                index=watchlink.split('<li data-index="')[i]
                index=index.split('"')[0]
                ref=domine+"wp-content/themes/"+theme+"/core.php?action=switch&index="+index+"&id="+ved_id
                w_link=req2(lin,ref)
                w_link=w_link.split('<iframe src="')[1]
                w_link=w_link.split('"')[0]
                
                if "//www"in w_link:
                    w_link=w_link.split("//www")[1]
                    w_link="https://www"+w_link
                if w_link in assessment_links:
                    pass
                else:  
                    if "https://watch" in w_link:  
                        pass
                    else:     
                    
                        assessment_links.append(w_link)
            except:
                pass
        if """')">Uptostream""" in watchlink:
            upto=watchlink.split("""('src','""")[1]
            upto=upto.split("""')">Uptostream""")[0]
            assessment_links.append(upto)
            
        BigArry['servers']=assessment_links

        data_d=req(lin)
        if '<li aria-label="download">'in data_d:
            # BigArry['download']={}
            downs =data_d.split('<li aria-label="download">')[1]
            downs =downs.split('</li>')[0]
            i=0
            all_links=[]
            try:
                for m in downs:
                    i+=1
                    down_l1 =downs.split('<a href="')[i]
                    down_l=down_l1.split('">')[0]
                    down_n=downs.split('<i class="fa fa-download"></i>\n')[i]
                    down_n=down_n.split('</a>')[0]
                    #BigArry['download']['name'+str(i)]=down_n
                    all_links.append(down_l)
            except:
                pass   
            BigArry['download']=all_links


  result = json.dumps(BigArry, ensure_ascii=False)
  
  return result
def run():
	app.run(host='0.0.0.0',port=8080)
t = Thread(target=run)
t.start()
