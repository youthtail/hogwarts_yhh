import requests
import logging
# 设置日志级别
logging.basicConfig(level=logging.INFO)

r = requests.get('https://www.cnblogs.com/lanyinhao/p/9634742.html', params={'name':'lily'})
r.encoding = 'ISO'
logging.info(f"我的=====，{r.url},\n{r.headers}\n{r.request}")
