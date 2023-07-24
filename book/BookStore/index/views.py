#from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

#def test_html(request):
    #t = loader.get_template('test.html')    #通过loader 加载test.html模板
    #html = t.render({'name':'c语言中文网'})   #用字典的方式传递变量并生成html
    #return HttpResponse(html)               #用响应对象将html的内容返回给浏览器

from django.shortcuts import render          #导入reder方法
def test(request):
    return render(request,'test.html',{'name':'c语言中文网'})    #根据字典数据生成动态模板

def test_html(request):
    #a = {}
    a={'name':'c语言中文网','course':['python','c''c++','java'],
       'b':{'name':'c语言中文网','address':'http://c.baincheng.net/'},
       'test_hello':test_hello,'class_obj':Websit()}
    return render(request,'test_html.html',a)
def test_hello():
    return '欢迎来到C语言中文网'
class Websit:
    def Web_name(self):
        return 'hello,c语言中文网'
    #Web_name.alters_date=Ture      #不让Websit()的方法被模板调用

def test_if(request):
    dic = {'x':2**4}
    return render(request,'test_if.html',dic)

from django.template import Template,Context
def Hello_MyWeb(request):
    #调用template()方法生成模板
    t = Template("""
                {% if web.name == 'c语言中文网' %}
                    {% if printable %}
                        <h1>Hello c语言中文网</h1>
                    {% else %}
                        <h2>欢迎你下次访问，c语言中文网</h2>
                    {% endif %}
                {% endif %}
            """)
    #Context必须是字典类型的对象，用来给模板传递参数
    c = Context({'web':{'name':'c语言中文网'},'printable':True})
    html = t.render(c)
    return HttpResponse(html)

def hello_myweb1(request):
    c = {'web':{'name':'c语言中文网'},'printable':True}
    return render(request,'hello_myweb1.html',c)

def test_for(request):
    #调用template()方法生成模板
    t1 = Template("""
            {% for item in list %}
                <li>{{item}}</li>
            {% empty %}
                <h1>如果找不到你想要的，可以来C语言中文网<br>(http://c.biancheng.net)</h1>
            {% endfor %}
            """)
    #调用context()方法给给模板传参
    #c1 = Context({'list':[]})
    c1 = Context({'list':['python','java','js','c++']})
    html = t1.render(c1)
    return HttpResponse(html)
