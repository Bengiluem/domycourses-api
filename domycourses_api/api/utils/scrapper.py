

def get_marmiton(url):
    print("Getting url: ", url)


def get_items(urls):
    print("URLS: ", urls)
    for url in urls:
        print("URL : ", url)
        if "https://www.marmiton.org/" in url:
            get_marmiton(url)
