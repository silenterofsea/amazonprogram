import time,hashlib,sys,os,json
import random
class bt_api:
    __BT_KEY = 'NYnZO1cZIUxviueNZbNSwqVp7vGky6f0'
    __BT_PANEL = 'http://79.143.62.21:8888'

    #如果希望多台面板，可以在实例化对象时，将面板地址与密钥传入
    def __init__(self,bt_panel = None,bt_key = None):
        if bt_panel:
            self.__BT_PANEL = bt_panel
            self.__BT_KEY = bt_key


    #取面板日志
    def get_logs(self):
        #拼接URL地址
        url = self.__BT_PANEL + '/data?action=getData'

        #准备POST数据
        p_data = self.__get_key_data()  #取签名
        p_data['table'] = 'logs'
        p_data['limit'] = 10
        p_data['tojs'] = 'test'

        #请求面板接口
        result = self.__http_post_cookie(url,p_data)

        #解析JSON数据
        return json.loads(result)

    def generate_random_str(self, randomlength):
      """
      生成一个指定长度的随机字符串
      """
      random_str = ''
      base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
      length = len(base_str) - 1
      for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
      return random_str

    # 创建一个邮箱
    def set_mail(self):
        # 拼接url
        url = self.__BT_PANEL + '/plugin?action=a&name=mail_sys&s=add_mailbox'

        # 准备POST数据
        p_data = self.__get_key_data()  #取签名
        p_data['quota'] = 5
        p_data['username'] =  self.generate_random_str(16) + '@infiniticloud.net'
        p_data['password'] = 'QWEqwe123！@#'
        p_data['full_name'] = 'alex'
        p_data['is_admin'] = 0

        #请求面板接口
        result = self.__http_post_cookie(url,p_data)

        return json.loads(result)

    def get_amazone_code(self, username):
        url = self.__BT_PANEL + '/plugin?action=a&name=mail_sys&s=get_mails'

        p_data = self.__get_key_data()  #取签名
        p_data['username'] = username
        p_data['p'] =  1

        #请求面板接口
        result = self.__http_post_cookie(url,p_data)
        result_json = json.loads(result)
        if len(result_json['data']) != 0:
            return result_json['data'][0]['html']
        else:
            # 长度为0,说明没有接受到邮件
            return False


    #计算MD5
    def __get_md5(self,s):
        m = hashlib.md5()
        m.update(s.encode('utf-8'))
        return m.hexdigest()

    #构造带有签名的关联数组
    def __get_key_data(self):
        now_time = int(time.time())
        p_data = {
                    'request_token':self.__get_md5(str(now_time) + '' + self.__get_md5(self.__BT_KEY)),
                    'request_time':now_time
                 }
        return p_data


    #发送POST请求并保存Cookie
    #@url 被请求的URL地址(必需)
    #@data POST参数，可以是字符串或字典(必需)
    #@timeout 超时时间默认1800秒
    #return string
    def __http_post_cookie(self,url,p_data,timeout=1800):
        cookie_file = './' + self.__get_md5(self.__BT_PANEL) + '.cookie';
        if sys.version_info[0] == 2:
            #Python2
            import urllib,urllib2,ssl,cookielib

            #创建cookie对象
            cookie_obj = cookielib.MozillaCookieJar(cookie_file)

            #加载已保存的cookie
            if os.path.exists(cookie_file):cookie_obj.load(cookie_file,ignore_discard=True,ignore_expires=True)

            ssl._create_default_https_context = ssl._create_unverified_context

            data = urllib.urlencode(p_data)
            req = urllib2.Request(url, data)
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_obj))
            response = opener.open(req,timeout=timeout)

            #保存cookie
            cookie_obj.save(ignore_discard=True, ignore_expires=True)
            return response.read()
        else:
            #Python3
            import urllib.request,ssl,http.cookiejar
            cookie_obj = http.cookiejar.MozillaCookieJar(cookie_file)
            if os.path.exists(cookie_file):cookie_obj.load(cookie_file,ignore_discard=True,ignore_expires=True)
            handler = urllib.request.HTTPCookieProcessor(cookie_obj)
            data = urllib.parse.urlencode(p_data).encode('utf-8')
            req = urllib.request.Request(url, data)
            opener = urllib.request.build_opener(handler)
            response = opener.open(req,timeout = timeout)
            cookie_obj.save(ignore_discard=True, ignore_expires=True)
            result = response.read()
            if type(result) == bytes: result = result.decode('utf-8')
            return result


if __name__ == '__main__':
    #实例化宝塔API对象
    my_api = bt_api()

    #调用get_logs方法
    r_data = my_api.set_mail()

    #打印响应数据
    print(r_data)
