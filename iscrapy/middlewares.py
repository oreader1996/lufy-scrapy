# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import anole
from scrapy import signals

from anole import UserAgent


# 随机生成UserAgent下载中间件
class CustomUserAgentDownloadMiddleware:
    def __init__(self):
        self.ua = UserAgent()

    def process_request(self, request, spider):
        agent = self.ua.random
        if agent:
            request.headers['User-Agent'] = agent
        else:
            request.headers[
                'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5410.0 Safari/537.36"


if __name__ == "__main__":
    # 测试生成随机user_agent
    user_agent = anole.UserAgent().random
    # 测试生成随机名字
    name = anole.Name().fake(surname="李")
    pass
