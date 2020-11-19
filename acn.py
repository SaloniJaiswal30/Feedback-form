from flask import Flask, render_template, request,flash,Markup, redirect, url_for
import datetime
from flaskext.mysql import MySQL
app = Flask(__name__,template_folder='C://Users/Saloni/.spyder-py3/templates/html_files')
mysql = MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'feedback'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
@app.route('/')
def student():
   return render_template('login.html')
#check for valid student or faculty
@app.route('/', methods=['POST'])
def my_form_post():
    
    c = mysql.connect().cursor()
    c.execute("SELECT * from form")
    data = c.fetchone()
    while data is not None:
        username = request.form['user']
        password = request.form['password']
        #cursor.execute("SELECT status from form where username=%s and pswd=%s",(username,password))
        #status=cursor.fetchone()
        #print(status[0])
        #print(data[0],data[1],data[2])
        if(username==data[0] and password==data[1] and data[2]=='y'):
            now = datetime.datetime.now()
            #print(now)
            #print(now.year,now.month,now.date)
            if(now.year==2020  and now.month==11 and (now.day==17 or now.day==18)):
            #flash('You were successfully logged in')
                return render_template('feedbackSystem.html')
            else:
                return "TIME OUT"
        data = c.fetchone()
    #c.execute("insert into faculty values(%s,%s)",("gita","123"))
    c.execute("SELECT * from faculty")   
    data = c.fetchone()
    while data is not None:
        username = request.form['user']
        password = request.form['password']
        #print("----",data[0],data[1])
        if(username==data[0] and password==data[1]):
            p = mysql.connect().cursor()
            p.execute("SELECT username from form")
            t=p.fetchall()
            return render_template('faculty.html',t=t)
        data = c.fetchone()
    return "incorrect user id or password or you are not registered by faculty"
#faculty register student
@app.route('/fac', methods=['POST'])
def fac():
    username=request.form['usr']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE form set status='y' where username=%s",(username))
    cursor.close()
    conn.commit()
    return "successfully registered"
#save feedback in database
@app.route('/login', methods=['POST'])
def feed():
    enroll=request.form['enroll']
    one=int(request.form['1'])
    two=int(request.form['2'])
    three=int(request.form['3'])
    four=int(request.form['4'])
    five=int(request.form['5'])
    six=int(request.form['6'])
    seven=int(request.form['7'])
    eight=int(request.form['8'])
    nine=int(request.form['9'])
    ten=int(request.form['10'])
    eleven=int(request.form['11'])
    twelve=int(request.form['12'])
    thirteen=int(request.form['13'])
    forteen=int(request.form['14'])
    fifteen=int(request.form['15'])
    sixteen=int(request.form['16'])
    seventeen=int(request.form['17'])
    eighteen=int(request.form['18'])
    ninteen=int(request.form['19'])
    twenty=int(request.form['20'])
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("insert into detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(enroll,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,forteen,fifteen,sixteen,seventeen,eighteen,ninteen,twenty))
    cursor.close()
    conn.commit()
    return redirect(url_for('student'))
#calculate no. of feedbacks and form chart
@app.route('/index', methods=['POST'])
def index(chartID = 'chart_ID', chart_type = 'bar', chart_height =1000):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=o6=o7=o8=o9=o10=o11=o12=o13=o14=o15=o16=o17=o18=o19=o20=o21=o22=o23=o24=o25=o26=o27=o28=o29=o30=0
    o2=o31=o32=o33=o34=o35=o36=o37=o38=o39=o40=o41=o42=o43=o44=o45=o46=o47=o48=o49=o50=o51=o52=o53=o54=o55=0
    o3=o56=o57=o58=o59=o60=o61=o62=o63=o64=o65=o66=o67=o68=o69=o70=o71=o72=o73=o74=o75=o76=o77=o78=o79=o80=0
    o4=o81=o82=o83=o84=o85=o86=o87=o88=o89=o90=o91=o92=o93=o94=o95=o96=o97=o98=o99=o100=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[1]==5):
            o5=o5+1
        if(d[1]==4):
            o4=o4+1
        if(d[1]==3):
            o3=o3+1
        if(d[1]==2):
            o2=o2+1
        if(d[1]==1):
            o1=o1+1 
        if(d[2]==5):
            o6=o6+1
        if(d[2]==4):
            o7=o7+1
        if(d[2]==3):
            o8=o8+1
        if(d[2]==2):
            o9=o9+1
        if(d[2]==1):
            o10=o10+1 
        if(d[3]==5):
            o11=o11+1
        if(d[3]==4):
            o12=12+1
        if(d[3]==3):
            o13=o13+1
        if(d[3]==2):
            o14=o14+1
        if(d[3]==1):
            o15=o15+1 
        if(d[4]==5):
            o16=o16+1
        if(d[4]==4):
            o17=o17+1
        if(d[4]==3):
            o18=o18+1
        if(d[4]==2):
            o19=o19+1
        if(d[4]==1):
            o20=o20+1
        if(d[5]==5):
            o21=o21+1
        if(d[5]==4):
            o22=o22+1
        if(d[5]==3):
            o23=o23+1
        if(d[5]==2):
            o24=o24+1
        if(d[5]==1):
            o25=o25+1 
        if(d[6]==5):
            o26=o26+1
        if(d[6]==4):
            o27=o27+1
        if(d[6]==3):
            o28=o28+1
        if(d[6]==2):
            o29=o29+1
        if(d[6]==1):
            o30=o30+1 
        if(d[7]==5):
            o31=o31+1
        if(d[7]==4):
            o32=o32+1
        if(d[7]==3):
            o33=o33+1
        if(d[7]==2):
            o34=o34+1
        if(d[7]==1):
            o35=o35+1 
        if(d[8]==5):
            o36=o36+1
        if(d[8]==4):
            o37=o37+1
        if(d[8]==3):
            o38=o38+1
        if(d[8]==2):
            o39=o39+1
        if(d[8]==1):
            o40=o40+1 
        if(d[9]==5):
            o41=o41+1
        if(d[9]==4):
            o42=o42+1
        if(d[9]==3):
            o43=o43+1
        if(d[9]==2):
            o44=o44+1
        if(d[9]==1):
            o45=o45+1 
        if(d[10]==5):
            o46=o46+1
        if(d[10]==4):
            o47=o47+1
        if(d[10]==3):
            o48=o48+1
        if(d[10]==2):
            o49=o49+1
        if(d[10]==1):
            o50=o50+1 
        if(d[11]==5):
            o51=o51+1
        if(d[11]==4):
            o52=o52+1
        if(d[11]==3):
            o53=o53+1
        if(d[11]==2):
            o54=o54+1
        if(d[11]==1):
            o55=o55+1
        if(d[12]==5):
            o56=o56+1
        if(d[12]==4):
            o57=o57+1
        if(d[12]==3):
            o58=o58+1
        if(d[12]==2):
            o59=o59+1
        if(d[12]==1):
            o60=o60+1 
        if(d[13]==5):
            o61=o61+1
        if(d[13]==4):
            o62=o62+1
        if(d[13]==3):
            o63=o63+1
        if(d[13]==2):
            o64=o64+1
        if(d[13]==1):
            o65=o65+1 
        if(d[14]==5):
            o66=o66+1
        if(d[14]==4):
            o67=o67+1
        if(d[14]==3):
            o68=o68+1
        if(d[14]==2):
            o69=o69+1
        if(d[14]==1):
            o70=o70+1
        if(d[15]==5):
            o71=o71+1
        if(d[15]==4):
            o72=o72+1
        if(d[15]==3):
            o73=o73+1
        if(d[15]==2):
            o74=o74+1
        if(d[15]==1):
            o75=o75+1 
        if(d[16]==5):
            o76=o76+1
        if(d[16]==4):
            o77=o77+1
        if(d[16]==3):
            o78=o78+1
        if(d[16]==2):
            o79=o79+1
        if(d[16]==1):
            o80=o80+1 
        if(d[17]==5):
            o81=o81+1
        if(d[17]==4):
            o82=o82+1
        if(d[17]==3):
            o83=o83+1
        if(d[17]==2):
            o84=o84+1
        if(d[17]==1):
            o85=o85+1
        if(d[18]==5):
            o86=o86+1
        if(d[18]==4):
            o87=o87+1
        if(d[18]==3):
            o88=o88+1
        if(d[18]==2):
            o89=o89+1
        if(d[18]==1):
            o90=o90+1 
        if(d[19]==5):
            o91=o91+1
        if(d[19]==4):
            o92=o92+1
        if(d[19]==3):
            o93=o93+1
        if(d[19]==2):
            o94=o94+1
        if(d[19]==1):
            o95=o95+1 
        if(d[20]==5):
            o96=o96+1
        if(d[20]==4):
            o97=o97+1
        if(d[20]==3):
            o98=o98+1
        if(d[20]==2):
            o99=o99+1
        if(d[20]==1):
            o100=o100+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]},{"name": 'Label2', "data": [o6,o7,o8,o9,o10]}, {"name": 'Label3', "data": [o11,o12,o13,o14,o15]}, {"name": 'Label4', "data": [o16,o17,o18,o19,o20]}, {"name": 'Label5', "data": [o21,o22,o23,o24,o25]}, {"name": 'Label6', "data": [o26,o27,o28,o29,o30]}, {"name": 'Label7', "data": [o31,o32,o33,o34,o35]}, {"name": 'Label8', "data": [o36,o37,o38,o39,o40]}, {"name": 'Label9', "data": [o41,o42,o43,o44,o45]}, {"name": 'Label10', "data": [o46,o47,o48,o49,o50]}, {"name": 'Label11', "data": [o51,o52,o53,o54,o55]}, {"name": 'Label12', "data": [o56,o57,o58,o59,o60]}, {"name": 'Label13', "data": [o61,o62,o63,o64,o65]}, {"name": 'Label14', "data": [o66,o67,o68,o69,o70]}, {"name": 'Label15', "data": [o71,o72,o73,o74,o75]}, {"name": 'Label16', "data": [o76,o77,o78,o79,o80]}, {"name": 'Label17', "data": [o81,o82,o83,o84,o85]}, {"name": 'Label18', "data": [o86,o87,o88,o89,o90]}, {"name": 'Label19', "data": [o91,o92,o93,o94,o95]}, {"name": 'Label20', "data": [o96,o97,o98,o99,o100]}]
    title = {"text": 'FeedBack'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, yAxis=yAxis, xAxis=xAxis)
@app.route('/index1', methods=['POST'])
def index1(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[1]==5):
            o5=o5+1
        if(d[1]==4):
            o4=o4+1
        if(d[1]==3):
            o3=o3+1
        if(d[1]==2):
            o2=o2+1
        if(d[1]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The course plan provided sufficient information on the objective and contents'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index2', methods=['POST'])
def index2(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[2]==5):
            o5=o5+1
        if(d[2]==4):
            o4=o4+1
        if(d[2]==3):
            o3=o3+1
        if(d[2]==2):
            o2=o2+1
        if(d[2]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The distribution of marks (for tests, assignments, tutorials and exams) was clearly stated in the course plan'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index3', methods=['POST'])
def index3(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[3]==5):
            o5=o5+1
        if(d[3]==4):
            o4=o4+1
        if(d[3]==3):
            o3=o3+1
        if(d[3]==2):
            o2=o2+1
        if(d[3]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'I found the course materials (class notes, handouts, prescribed textbook) useful'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index4', methods=['POST'])
def index4(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[4]==5):
            o5=o5+1
        if(d[4]==4):
            o4=o4+1
        if(d[4]==3):
            o3=o3+1
        if(d[4]==2):
            o2=o2+1
        if(d[4]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The assignments, tutorials, quizzes etc, helped me to understand the course'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index5', methods=['POST'])
def index5(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[5]==5):
            o5=o5+1
        if(d[5]==4):
            o4=o4+1
        if(d[5]==3):
            o3=o3+1
        if(d[5]==2):
            o2=o2+1
        if(d[5]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The tests and examination covered to a large extent was taught in the class'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index6', methods=['POST'])
def index6(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[6]==5):
            o5=o5+1
        if(d[6]==4):
            o4=o4+1
        if(d[6]==3):
            o3=o3+1
        if(d[6]==2):
            o2=o2+1
        if(d[6]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'I was stisfied with the course coverage'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index7', methods=['POST'])
def index7(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[7]==5):
            o5=o5+1
        if(d[7]==4):
            o4=o4+1
        if(d[7]==3):
            o3=o3+1
        if(d[7]==2):
            o2=o2+1
        if(d[7]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The evaluation was fair and transparent'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index8', methods=['POST'])
def index8(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        #print(d[8])
        if(d[8]==5):
            o5=o5+1
        if(d[8]==4):
            o4=o4+1
        if(d[8]==3):
            o3=o3+1
        if(d[8]==2):
            o2=o2+1
        if(d[8]==1):
            o1=o1+1 
        d = l.fetchone()
    #print(o1,o2,o3,o4,o5)
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The course helped me to acquire knowledge and skills'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index9', methods=['POST'])
def index9(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[9]==5):
            o5=o5+1
        if(d[9]==4):
            o4=o4+1
        if(d[9]==3):
            o3=o3+1
        if(d[9]==2):
            o2=o2+1
        if(d[9]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text10": 'This course motivated me to learn more'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index10', methods=['POST'])
def index10(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[10]==5):
            o5=o5+1
        if(d[10]==4):
            o4=o4+1
        if(d[10]==3):
            o3=o3+1
        if(d[10]==2):
            o2=o2+1
        if(d[10]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'Overall, the course was stisfactory'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index11',methods=['POST'])
def index11(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[11]==5):
            o5=o5+1
        if(d[11]==4):
            o4=o4+1
        if(d[11]==3):
            o3=o3+1
        if(d[11]==2):
            o2=o2+1
        if(d[11]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The instructor was generally well prepared for the classes'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index12', methods=['POST'])
def index12(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[12]==5):
            o5=o5+1
        if(d[12]==4):
            o4=o4+1
        if(d[12]==3):
            o3=o3+1
        if(d[12]==2):
            o2=o2+1
        if(d[12]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The instructor presented the contents effectively'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index13', methods=['POST'])
def index13(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[13]==5):
            o5=o5+1
        if(d[13]==4):
            o4=o4+1
        if(d[13]==3):
            o3=o3+1
        if(d[13]==2):
            o2=o2+1
        if(d[13]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The instructor generated interest in the subject'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index14', methods=['POST'])
def index14(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[14]==5):
            o5=o5+1
        if(d[14]==4):
            o4=o4+1
        if(d[14]==3):
            o3=o3+1
        if(d[14]==2):
            o2=o2+1
        if(d[14]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The instructor delivered the lecturers  at an appropriate pace'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index15', methods=['POST'])
def index15(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[15]==5):
            o5=o5+1
        if(d[15]==4):
            o4=o4+1
        if(d[15]==3):
            o3=o3+1
        if(d[15]==2):
            o2=o2+1
        if(d[15]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The instructor made use of appropriate teaching aids and methods'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index16', methods=['POST'])
def index16(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[16]==5):
            o5=o5+1
        if(d[16]==4):
            o4=o4+1
        if(d[16]==3):
            o3=o3+1
        if(d[16]==2):
            o2=o2+1
        if(d[16]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The instructor encouraged students participation and interaction in the class'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index17', methods=['POST'])
def index17(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[17]==5):
            o5=o5+1
        if(d[17]==4):
            o4=o4+1
        if(d[17]==3):
            o3=o3+1
        if(d[17]==2):
            o2=o2+1
        if(d[17]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The instructor provided timely and effective feedback regarding the assignment/test/exams'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index18', methods=['POST'])
def index18(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[18]==5):
            o5=o5+1
        if(d[18]==4):
            o4=o4+1
        if(d[18]==3):
            o3=o3+1
        if(d[18]==2):
            o2=o2+1
        if(d[18]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The instructor was available outside class hour for consultation'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index19',methods=['POST'])
def index19(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[19]==5):
            o5=o5+1
        if(d[19]==4):
            o4=o4+1
        if(d[19]==3):
            o3=o3+1
        if(d[19]==2):
            o2=o2+1
        if(d[19]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'The instructor was regulas to the class'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
@app.route('/index20',methods=['POST'])
def index20(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    conn = mysql.connect()
    l = conn.cursor()
    l.execute("SELECT * from detail")
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    d = l.fetchone()
    while d is not None:
        if(d[20]==5):
            o5=o5+1
        if(d[20]==4):
            o4=o4+1
        if(d[20]==3):
            o3=o3+1
        if(d[20]==2):
            o2=o2+1
        if(d[20]==1):
            o1=o1+1 
        d = l.fetchone()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Label1', "data": [o1,o2,o3,o4,o5]}]
    title = {"text": 'Overall, the instructor was effective in his/her roll as a teacher'}
    xAxis = {"categories": ['1','2','3','4','5']}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
if __name__ == "__main__":
    app.run()