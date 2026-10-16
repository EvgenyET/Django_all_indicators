from django.shortcuts import render
import os
import shutil
# from plotly_charts import script
from App.plotly_charts import script

'''Создаём функцию, которая рендерит страницу для Django и 
rопирует файл chart.html из каталога "App" в каталог "templates" используя относительный путь:'''

def page3(request):
    script()
    src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chart.html')
    dst_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
    shutil.copy2(src_path, dst_path)
    return render(request, 'chart.html')