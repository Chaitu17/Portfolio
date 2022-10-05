from bs4 import BeautifulSoup
import requests

URL=" https://www.aarogyasetu.gov.in/."
page=requests.get(URL)
soup=BeautifulSoup(page.content,"lxml")
a=soup.find("a",class_="view_state")
States_link=a.attrs
page_S=requests.get("http:"+States_link["href"])
soup_S=BeautifulSoup(page_S.content,"lxml")

State_AP=soup_S.find("div",class_="field-item odd").find_all("div",class_="field-item even")
State_Name=State_AP[0].contents[0]
Total_No=int(State_AP[1].contents[0])
Cured_No=int(State_AP[2].contents[0])
Deaths=int(State_AP[3].contents[0])
Active_cases=Total_No-(Cured_No + Deaths)

#print "State=",State_Name,"\n\tTotal No. Covid cases=",Total_No,"\n\tCured No. of cases=",Cured_No,"\n\tNo. of Deaths=",Deaths

#print "\tActive No. Cases=",Active_cases

State_TS=soup_S.find_all("div",class_="field-item odd")[15].find_all("div",class_="field-item even")
State_Name=State_TS[0].contents[0]
Total_Num=int(State_TS[1].contents[0])
Cured_Num=int(State_TS[2].contents[0])
Death_Num=int(State_TS[3].contents[0])
Active_Num=Total_Num-(Cured_Num + Death_Num)

#print "State=",State_Name,"\n\tTotal No. Covid cases=",Total_Num,"\n\tCured No. of cases=",Cured_Num,"\n\tNo. of Deaths=",Death_Num

#print "\tActive No. Cases=",Active_Num

AP=str(Active_cases)
TS=str(Active_Num)

f = open("first.html","w")

message = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
    <link rel="stylesheet" href="styling.css">
    <script src="https://use.fontawesome.com/d1341f9b7a.js"></script>
</head>
<body>
    <header>
        <div class="nav-bar">
            <ul>
                <li><a href="first.html">HOME</a></li>
                <li><a href="interests.html">INTERESTS</a></li>
                <li><a href="skills.html">SKILLS</a></li>
                <li><a href="hobbies.html">HOBBIES</a></li>
            </ul>
        </div>
    </header>
    <div class="box">
        <img src="profile.jpg" alt="" class="profile-pic">
        <h1>Krishna Chaitanya</h1>
        <h6>Quantum Computing and Machine Learning Enthusiast</h6>
        <p>I'm willing to work on Quantum Computing and Machine Learning Projects and open to any kind of internships or job offers.</p>
        <ul>
            <li><a href="https://www.facebook.com/chaitanya.aleti.9"><i class="fa fa-facebook-square" aria-hidden="true"></i></a></li>
            <li><a href="https://twitter.com/ChaitanyaAleti"><i class="fa fa-twitter-square" aria-hidden="true"></i></a></li>
            <li><a href="https://www.youtube.com/channel/UCVahCkJwMe2ZXzC88b7xOJQ"><i class="fa fa-youtube-square" aria-hidden="true"></i></a></li>
        </ul>
    </div>
    <div class="box">
	<li>Andhra Pradesh - No of active COVID cases : """+ AP +"""</li>
	<li>Telangana - No of active COVID cases : """+ TS +"""</li>
    </div>
</body>
</html>"""

f.write(message)
f.close()





