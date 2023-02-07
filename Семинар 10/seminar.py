def decorator(func):
    import time
    def wripper(url):
        start = time.time()
        response = func(url)
        end = time.time()
        print("Время выполенения функции", (end-start)," секунд")
        return response
    return wripper

@decorator
def request_url(url):
    import requests
    response = requests.get(url)
    return response


url = "https://mail.yandex.ru/?utm_source=main_stripe_big&uid=3500212#inbox"
print(request_url(url))

url = "https://dzen.ru/news/story/EHks-premer_Izrailya_Bennet_Putin_vnachale_specoperacii_poobeshhal_ne_ustranyat_Zelenskogo--8e5943fca52175f21c58f55491e4b3cb?lang=ru&fan=1&stid=NV-2lY6uh1BgoY7TJmN1&t=1675583835&tt=true&persistent_id=1810161454&story=c3cdca20-276b-5c6a-aa18-18090b957551&issue_tld=ru"
print(request_url(url))