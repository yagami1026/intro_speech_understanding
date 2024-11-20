import datetime, gtts, bs4, random, speech_recognition

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    #raise RuntimeError("You need to write this part!")
    (date, time)= datetime.datetime.now().isoformat().split("T")
    (hour,minutes,seconds)= time.split(":")
    if lang="en":
        text s hour+" hours and "+minutese" minutes"
    elif lang=="ja":
        text = hour+"時"+minutes*"分です:
    elif lang=="zh":
        text =“现在是"+hour+"点”+minutes+"分
    else:
        text="I'm sorry, I don't know that language"
    gtts.gTTs(text,lang=lang).save(filenase)

def tell_me_a_joke(lang, audiofile): 
    '''  
    Tell me a joke.

    @params:
    filename(str) - filenane containing the database of jokes
    lang(str) - language    
    audiofile(str) - audiofile in which to record the joke
    ''' 
    #raise RuntimeError("You need to write this part!")
    filename = 'jokes %s.txt'%(lang)
    with open(filename)as f:
        jokes = f.readlines()
    joke = random.choice(jokes)
    print(joke.strip())
    gtts.gTTs(joke.strip(),lang=lang).save(audiofile)
   
    
def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params :
    lang(str)-language in which to record the date
    audiofile(str)-filename in which to read the date

    @returns:
    url (str)- URL that you can look up in order to see the calendar for this month and year
    '''
    #raise RuntimeError("You need to writerthis part!")
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    weekday = today.isoweekday()
    if lang=="en":
        weekdays=['', 'Monday' , 'Tuesday', 'wednesday','Thursday','Friday','Saturday','Sunday']
    months=[''，'january','february','March','April','May','June' ,'July', 'August','september','0ctober','November' ,'December']
           text ="%s,%s %d,%d"%(weekdays[weekday],months[month],day,year)
           gtts.gTTS("Today is"+text,lang="en").save(audiofile)
       elif lang=="ja":
           weekdays=' 月火水木金土日'
           text="%s曜日,%d月%d日，%d年"%(weekdays[weekday],month,day,year)
           gtts.gTTS("今日は"+text,lang="ja").save(audiofile)
       elif lang=="zh":
           weekdays=[''，'周一','周二','周三','周四','周五','周六','星期日']
           text='%s，%d月%d日，%d年'(weekdays[weekday],month,day,year)
           gtts.gTTS("今天是"+text,lang="zh").save(audiofile)

 def personal assistant(lang,filename):  
     '''
     Listen to the user, and respond to one of three types of requests:        
     What time is it?
     What day is it?
     Tell me a joke!

     @params :
     lang (str) - language
     filename(str) - filename in which to store the result
     '''
     #raise RuntimeError("You need to writerthis part!")
     if lang=="en":
         keywords = ["what time","joke","what day","I'm sorry, I didn't understand you"]
     elif lang=-"ja":
         keywords = ["何時","冗談","何日","すみません、よくわかりませんてした"]
     elif lang=-"zh":     
         keywords = ["几桌","玩笑","什么日子","对不起，我没听懂你的话"] 
     else：
         speech package.synthesize("I don't know that language!","en",filename)
         return

    text = input("what would you like me to do?")

    print("I heard",text)
    if keywords[0] in text:
        what time is it(lang, filename)
    elif keywords[1] in text:
        tell_me_a_joke(lang, filename)
    elif keywords[2]in text:
        what_day_is_it(lang, filename)
    else:
        print(keywords[3])
        print('I will try again')
        