import cx_Oracle
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import chart_studio
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard

chart_studio.tools.set_credentials_file(username='kKravtsova', api_key='ZsoDFDqUDYzaPIAtQscH')
con = cx_Oracle.connect('test/passtest@//localhost:8080/xe')
cursor = con.cursor()


def fileId_from_url(url):
    url_raw = url.split('/')
    cleared = [s.strip('~') for s in url_raw]  # remove the ~
    nickname = cleared[3]
    id = cleared[4]
    fileId = nickname + ':' + id
    return fileId


request_1 = """
select country_name,COUNT(*) as cnt
from insurance_info
group by country_name
order by COUNT(*) desc
FETCH FIRST 10 ROWS ONLY;
"""

cursor.execute(request_1)

x_request_1 = list()
y_request_1 = list()

for country_name, cnt in cursor:
    x_request_1.append(cnt)
    y_request_1.append(country_name)
    print(x_request_1)
    print(y_request_1)

request_2 = """
select dis_channel,COUNT(*)
from insurance_info
GROUP BY dis_channel;
"""

cursor.execute(request_2)

x_request_2 = list()
y_request_2 = list()

for dis_channel, cnt in cursor:
    x_request_2.append(cnt)
    y_request_2.append(dis_channel)


request_3 = """
select human_trip.country_name,max(commision)
from insurance_info
group by human_trip.country_name
having max(commision) > 150;
"""

cursor.execute(request_3)

x_request_3 = list()
y_request_3 = list()

for DESTIN_1,max_value in cursor:
    x_request_3.append(ESTIN_1)
    y_request_3.append(max_value)

bar = go.Bar(
    y=x_request_1,
    x=y_request_1
)
graph_request_1 = py.plot([bar], auto_open=False, filename='request_1')

pie = go.Pie(
    labels=x_request_2,
    values=y_request_2
)
graph_request_2 = py.plot([pie], auto_open=False, filename='request_2')

scatter = go.Scatter(
    x=x_request_3,
    y=y_request_3
)
graph_request_3 = py.plot([scatter], auto_open=False, filename='request_3')

cursor.close()
con.close()

MyBoard1 = dashboard.Dashboard()
dia_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_from_url(graph_request_1),
    'title': 'Запит 1: вивести топ 10 країн з максимальною відвідуваносю'
}
dia_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_from_url(graph_request_2),
    'title': 'Запит 2: вивести відсоток онлайн та офлайн страхувань',

}
dia_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_from_url(graph_request_3),
    'title': 'Запит 3: розподіл максимальної комісії за країною,де комісія більше за 150'
}

MyBoard1.insert(dia_1)
MyBoard1.insert(dia_2, 'below', 1)
MyBoard1.insert(dia_3, 'right', 2)

py.dashboard_ops.upload(MyBoard1, 'LAB2_Kravtsova')