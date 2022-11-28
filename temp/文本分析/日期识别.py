import re
from datetime import datetime, timedelta
from dateutil.parser import parse
import jieba.posseg as psg
def check_time_valid(word):
    # 对提取的拼接日期串进行进一步处理，以进行有效性判断
    m = re.match("\d+$", word)
    if m:
        if len(word) <= 6:
            return None
    word1 = re.sub('[号|日]\d+$', '日', word)
    if word1 != word:
        return check_time_valid(word1)
    else:
        return word1
UTIL_CN_NUM = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4,
'五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
'5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}
UTIL_CN_UNIT = {'十': 10, '百': 100, '千': 1000, '万': 10000}


def cn2dig(src):
    if src == "":
        return None
    m = re.match("\d+", src)
    if m:
        return int(m.group(0))
    rsl = 0
    unit = 1
    for item in src[::-1]:
        if item in UTIL_CN_UNIT.keys():
            unit = UTIL_CN_UNIT[item]
        elif item in UTIL_CN_NUM.keys():
            num = UTIL_CN_NUM[item]
            rsl += num * unit
        else:
            return None
    if rsl < unit:
        rsl += unit
    return rsl
def year2dig(year):
    res = ''
    for item in year:
        if item in UTIL_CN_NUM.keys():
            res = res + str(UTIL_CN_NUM[item])
        else:
            res = res + item
    m = re.match("\d+", res)
    if m:
        if len(m.group(0)) == 2:
            return int(datetime.datetime.today().year/100)*100 + int(m.group(0))
        else:
            return int(m.group(0))
    else:
        return None
def parse_datetime(msg):
    # 将每个提取到的文本日期串进行时间转换。
    # print("parse_datetime开始处理：",msg)
    if msg is None or len(msg) == 0:
        return None
    try:
        msg = re.sub("年"," ",msg)# parse不认识"年"字
        dt = parse(msg, yearfirst=True, fuzzy=True)
        # print(dt)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        m = re.match(r"([0-9零一二两三四五六七八九十]+年)?([0-9一二两三四五六七八九十]+月)?([0-9一二两三四五六七八九十]+[号日])?([上中下午晚早]+)?([0-9零一二两三四五六七八九十百]+[点:\.时])?([0-9零一二三四五六七八九十百]+分?)?([0-9零一二三四五六七八九十百]+秒)?",
                    msg)
        if m.group(0) is not None:
            res = {
                "year": m.group(1),
                "month": m.group(2),
                "day": m.group(3),
                "hour": m.group(5) if m.group(5) is not None else '00',
                "minute": m.group(6) if m.group(6) is not None else '00',
                "second": m.group(7) if m.group(7) is not None else '00',
            }
            params = {}

            for name in res:
                if res[name] is not None and len(res[name]) != 0:
                    tmp = None
                    if name == 'year':
                        tmp = year2dig(res[name][:-1])
                    else:
                        tmp = cn2dig(res[name][:-1])
                    if tmp is not None:
                        params[name] = int(tmp)
            target_date = datetime.today().replace(**params)
            is_pm = m.group(4)
            if is_pm is not None:
                if is_pm == u'下午' or is_pm == u'晚上' or is_pm =='中午':
                    hour = target_date.time().hour
                    if hour < 12:
                        target_date = target_date.replace(hour=hour + 12)
            return target_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return None
def time_extract(text):
    time_res = []
    word = ''
    keyDate = {'今天': 0, '至今': 0, '明天':1, '后天': 2}
    for k, v in psg.cut(text):
        if k in keyDate:
            if word != '':
                time_res.append(word)
            word = (datetime.today() + timedelta(days=keyDate.get(k, 0))).strftime('%Y年%m月%d日')
        elif word != '':
            if v in ['m', 't']:
                word = word + k
            else:
                time_res.append(word)
                word = ''
        elif v in ['m', 't']:
            word = k
    if word != '':
        time_res.append(word)
    # print('22222222',time_res)
    result = list(filter(lambda x: x is not None, [check_time_valid(w) for w in time_res]))
    final_res = [parse_datetime(w) for w in result]
    return [x for x in final_res if x is not None]

def yanZhengRightData(string):
    m = re.match("(\d{4}|\d{2})-(\d{2}|\d{1})-(\d{2}|\d{1})", string)
    if m:
        return True
    else:
        return time_extract(string)
if __name__ == '__main__':
    print(time_extract("从2016年3月5日至今"))
    print(time_extract("在20160824-20180529的全部交易。"))
    print(time_extract("2017.6.12-7.10交！"))
    print(yanZhengRightData("2017-12-21"))
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author:SingWeek
 
import re
from datetime import datetime,timedelta
from dateutil.parser import parse
import jieba.posseg as psg
 
UTIL_CN_NUM={'零':0,'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
UTIL_CN_UNIT={'十':10,'百':100,'千':1000,'万':10000}
 
def get_lastweek(day=1):
    d = datetime.now()
    dayscount = timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = timedelta(days=7-day)
    dayfrom = dayto - sixdays
    date_from = datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    return str(date_from)[0:4]+'年'+str(date_from)[5:7]+'月'+str(date_from)[8:10]+'日'
 
def get_nextweek(day=1):
    d = datetime.now()
    dayscount = timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = timedelta(days=-7-day)
    dayfrom = dayto - sixdays
    date_from = datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    return str(date_from)[0:4]+'年'+str(date_from)[5:7]+'月'+str(date_from)[8:10]+'日'
 
def get_week(day=1):
    d = datetime.now()
    dayscount = timedelta(days=d.isoweekday())
    dayto = d - dayscount
    sixdays = timedelta(days=-day)
    dayfrom = dayto - sixdays
    date_from = datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
    return str(date_from)[0:4]+'年'+str(date_from)[5:7]+'月'+str(date_from)[8:10]+'日'
 
def check_time_valid(word):
    m=re.match("\d+$",word)
    if m:
        if len(word)<=6:
            return None
    word1=re.sub('[号|日]\d+$','日',word)
    if word1!=word:
        return check_time_valid(word)
    else:
        return word1
 
def cn2dig(src):
    if src=="":
        return None
    m=re.match("\d+",src)
    if m:
        return int(m.group(0))
    rsl=0
    unit=1
    for item in src[::-1]:
        if item in UTIL_CN_UNIT.keys():
            unit=UTIL_CN_UNIT[item]
        elif item in UTIL_CN_NUM.keys():
            num=UTIL_CN_NUM[item]
            rsl+=num*unit
        else:
            return None
    if rsl<unit:
        rsl+=unit
    return rsl
 
def year2dig(year):
    res=''
    for item in year:
        if item in UTIL_CN_NUM.keys():
            res=res+str(UTIL_CN_NUM[item])
        else:
            res=res+item
    m=re.match("\d+",res)
    if m:
        if len(m.group(0))==2:
            return int(datetime.today().year/100)*100+int(m.group(0))
        else:
            return int(m.group(0))
    else:
        return None
 
def parse_datetime(msg):
    tmptime= datetime.today().strftime('%Y{y}%m{m}%d{d}%H{h}%M{m}%S{s}').format(y='年',m='月',d='日', h='时', M='分',s='秒')#获取年月日时分秒
    if msg is None or len(msg)==0:
        return None
    try:
        dt=parse(msg,fuzzy=True)
        return dt.strftime('%Y-%m-%d %H:%M:%s')
    except Exception as e:
        m = re.match("([0-9零一二三四五六七八九十]+年)?([0-9零一二三四五六七八九十]+月)?([0-9零一二三四五六七八九十]+[号日])?([上中下午晚早]+)?([0-9零一二三四五六七八九十百]+[点:时])?([0-9零一二三四五六七八九十百]+分)?([0-9零一二三四五六七八九十百]+秒)?",msg)
        if m.group(0) is not None:
            res={"year":m.group(1) if m.group(1) is not None else str(tmptime[0:5]),
                 "month":m.group(2) if m.group(2) is not None else str(tmptime[5:8]),
                 "day":m.group(3) if m.group(3) is not None else str(tmptime[8:11]),
                 "hour":m.group(5) if m.group(5) is not None else '00',
                 "minute": m.group(6) if m.group(6) is not None else '00',
                 "second": m.group(7) if m.group(7) is not None else '00',}
            # print("匹配",res)
            params={}
            for name in res:
                if res[name] is not None and len(res[name]) !=0:
                    tmp=None
                    if name=='year':
                        tmp=year2dig(res[name][:-1])
                    else:#时间格式转换
                        tmp=cn2dig(res[name][:-1])
                    if tmp is not None:
                        params[name]=int(tmp)
            # print("----------------------》",params)
            target_date=datetime.today().replace(**params)#用新的时间参数替换当前的时间
            is_pm=m.group(4)
            if is_pm is not None:
                if is_pm==u'下午' or is_pm==u'晚上' or is_pm=='中午':
                    hour=params['hour']
                    if hour<12:
                        target_date=target_date.replace(hour=hour+12)
            return target_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return None
 
def time_extract(text):
    time_res=[]
    word=''
    keyDate={'今天':0,'明天':1,'后天':2,'昨天':-1,'前天':-2}
    timedic=['时','分','到']
    tmptext=[]
    for k,v in psg.cut(text):
        tmptext.append([k,v])
    for i in range(len(tmptext)):
        k,v=tmptext[i][0],tmptext[i][1]
        if k in keyDate:#今天、明天、后天、昨天、前天具体时间提取计算
            word = (datetime.today() + timedelta(days=keyDate.get(k, 0))).strftime('%Y{y}%m{m}%d{d}').format(y='年',m='月',d='日')
        elif k =='到':#时间段提取
            if word!='':
                time_res.append(word)
                word = ''
        elif word != '':
            if v in ['m', 't']:
                try:
                    if tmptext[i+1][0] in timedic:
                        word = word + k+tmptext[i+1][0]
                    else:
                        word = word + k
                except:
                    word = word + k
            elif k not in timedic:
                time_res.append(word)
                word = ''
        elif v in ['m', 't']:
            word = k
    if word != '':
        time_res.append(word)
    tmp_time_res = []
    for i in range(len(time_res)):
        if time_res[i][:2] in ['上周','下周']:
            if time_res[i][2:3] in UTIL_CN_NUM.keys():
                day=UTIL_CN_NUM[time_res[i][2:3]]
                if time_res[i][:2]=='上周':
                    tmp_time_res.append(get_lastweek(day)+time_res[i][3:])
                else:
                    tmp_time_res.append(get_nextweek(day) + time_res[i][3:])
        elif time_res[i][:1] == '周':
            if time_res[i][1:2] in UTIL_CN_NUM.keys():
                day=UTIL_CN_NUM[time_res[i][1:2]]
                if time_res[i][:1]=='周':
                    tmp_time_res.append(get_week(day)+time_res[i][2:])
        else:
            tmp_time_res.append(time_res[i])
    time_res=tmp_time_res
    try:
        print("匹配字符串：",time_res)
        result=list(filter(lambda x:x is not None, [check_time_valid(w) for w in time_res]))
        final_res=[parse_datetime(w) for w in result]
        return [x for x in final_res if x is not None]
    except:
        return None
 
# test1="我要预定2019年1月28号3时10分27秒房间"
# test1="预定2019年1月28号下午3时10分27秒住到2019年3月17号"
# test1="我要订今天到明天的房间"
# test1="15号行程安排"
# test1="上周一下午5点集合"
# test1="27号到30号"
test1="今天多少号"
print(test1,time_extract(test1),sep=":")
