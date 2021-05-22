from dummy_server.server import get_random_request


class Request():
    def __init__(self, type, ts, content):
        self.type = type
        self.ts = Time_Worck(ts)
        self.content = content

    def sort_by_type(self):
        pass

    def response(self):
        pass


class Time_Worck():
    def __init__(self, ts):
        self.ts = ts

    def is_weekend(self):
        pass


def text_processing(is_weekend, day_of_week, content):
    pass


def image_processing(content, one_day_ago):
    pass


def video_processing(is_weekend, content):
    pass


def sound_processing(content):
    pass


if __name__ == '__main__':
    for _ in range(10):
        request = get_random_request()
        print(request)
        print(Request(*request).response())
