from dummy_server.server import get_random_request
from time import time
import re


class Request():
    def __init__(self, type, ts, content):
        self.type = type
        self.ts = Time_Worck(ts)
        self.content = content

    def sort_by_type(self):
        if self.type == 'text':
            return text_processing(
                self.ts.is_weekend(),
                self.ts.day_of_week(),
                self.content
            )
        elif self.type == 'image':
            return image_processing(
                self.content,
                self.ts.one_day_ago()
            )
        elif self.type == 'video':
            return video_processing(
                self.ts.is_weekend(),
                self.content
            )
        elif self.type == 'sound':
            return sound_processing(
                self.content
            )
        else:
            return 'Wrong type'

    def response(self):
        return self.sort_by_type()


class Time_Worck():
    def __init__(self, ts):
        self.ts = ts

    def is_weekend(self):
        if (self.ts.weekday() in (5, 6)):
            return True
        else:
            return False

    def day_of_week(self):
        return self.ts.weekday()

    def one_day_ago(self):
        return (self.ts.fromtimestamp(time() - 86400))


def text_processing(is_weekend, day_of_week, content):
    if is_weekend is True:
        if day_of_week == 5:
            return '\N{Circled Digit Six}'
        else:
            return '\N{Circled Digit Seven}'
    else:
        return len(set(content.lower().split(' ')))


def image_processing(content, one_day_ago):
    check_jpg = re.findall(r'.jpg', content)
    if check_jpg == ['.jpg']:
        return (re.findall(r'(\w+)\.', content))
    else:
        return one_day_ago


def video_processing(is_weekend, content):
    len_ext_cont = len(re.findall(r'\.(\w+)', content))
    if is_weekend is True:
        if len_ext_cont == 4:
            return 'OK'
        else:
            return 'REJECT'
    else:
        if len_ext_cont == 3:
            return 'OK'
        else:
            return 'REJECT'


def sound_processing(content):
    simbols = (re.findall(r'\w', content))
    main_dict = {}
    flag = 0
    for sim in simbols:
        main_dict[sim] = main_dict.get(sim, 0) + 1
    for sim in main_dict:
        if main_dict[sim] == 1:
            flag = 1
            return sim
    if flag == 0:
        return 'None'


if __name__ == '__main__':
    for _ in range(10):
        request = get_random_request()
        print(request)
        print(Request(request['type'], request['ts'],
              request['content']).response())
