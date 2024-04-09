from anole import UserAgent


# 随机生成UserAgent下载中间件
class UserAgentDownloadMiddleware:
    ua = None
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5410.0 Safari/537.36"

    def __init__(self):
        self.ua = UserAgent()

    def process_request(self, request, spider):
        ua_random = self.ua.random
        request.headers['User-Agent'] = ua_random if ua_random else self.user_agent


if __name__ == "__main__":
    import anole

    # 测试生成随机user_agent
    user_agent = anole.UserAgent().random
    # 测试生成随机名字
    name = anole.Name().fake(surname="李")
    pass
