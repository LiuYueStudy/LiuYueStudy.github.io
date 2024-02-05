from pydoc import html

from flask import Flask, render_template, request, Response

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    # 接收前端ajax发送的请求
    prey = request.form.get("uid")
    # print(prey)

    # 数据读取
    datalist = []
    with open('test.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip('\n')
            if line == None:
                pass
            else:
                data = dict(prey=str(line))
                if data['prey'] != None:
                    datalist.append(data)
    # print(datalist)

    # 数据写入
    with open('test.txt', 'a+', encoding="utf-8") as f:
        if prey == None:
            pass
        else:
            f.write(str(prey) + '\n')

    if request.method == "GET":
        return render_template("index.html", datalist=datalist)

    # 数据传入
    return render_template("index.html", datalist=datalist)

# 测试网页
@app.route('/test2',methods=["GET","POST"])
def test2():
    # 接收前端ajax发送的请求
    prey=request.form.get("uid")
    # print(prey)

    # 数据读取
    datalist=[]
    with open('test1.txt','r',encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip('\n')
            if line ==None:
                pass
            else:
                data=dict(prey=str(line))
                if data['prey']!=None:
                    datalist.append(data)
    print(datalist)

    # 数据写入
    with open('test.txt','a+',encoding="utf-8") as f:
        if prey==None:
            pass
        else:
            f.write(str(prey)+'\n')

    if request.method=="GET":
        return render_template("test_3.html",datalist=datalist)

    # 数据传入
    return render_template("test_3.html",datalist=datalist)


@app.route('/test1')
def test1():
    # return render_template("test_1.html")
    return render_template("test_56.html")

@app.route('/yanhua')
def yanhua():
    return render_template('index_flower.html')

if __name__ == '__main__':
    app.run()
