#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：Valuebai
@Date   ：2019/10/31 19:58
@Desc   ：
=================================================='''

from flask import Flask, render_template

from APP.SentimentAnalysis.dianping_blueprint import app_dianping
from APP.TextSummarization.text_blueprint import app_summarization
from os.path import abspath, dirname
from conf.logConf import logger


app = Flask("__main__", static_folder='static', template_folder='templates')

# 使用blueprint注册蓝图分隔视图
app.register_blueprint(app_dianping, url_prefix="/SentimentAnalysis")
app.register_blueprint(app_summarization, url_prefix="/TextSummarization")
app.root_path = abspath(dirname(__file__))


# 展示网站主页
@app.route('/', methods=['GET', 'POST'])
def index():
    logger.info('访问home.html')
    logger.info("$_$ kill_bug_team run, to the moon $_$")
    return render_template('home.html')


if __name__ == "__main__":
    app.debug = True
    logger.info('项目运行，GO')

    # main run
    app.run(host='0.0.0.0', port=8688)
