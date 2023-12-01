#-- Multiprocessing

import concurrent.futures
import time


def runMProcess(data, function):
    # Max number of threads = 4
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(function, url): url for url in data}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                # print('%r page is %d bytes' % (url, len(data)))
                pass

def runMProcessWithReturn(data, function):
    datas = []
    # Max number of threads = 4
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(function, url): url for url in data}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                # print('%r page is %d bytes' % (url, len(data)))
                # print('%r page is %d bytes' % (url, len(data)))
                datas.append(data)
    return datas



