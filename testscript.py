import requests

urls = []

urls.append("http://127.0.0.1:5000/fog/add/?id=1&lat=9.456&long=145.56&cpuTime=42")
urls.append("http://127.0.0.1:5000/fog/add/?id=2&lat=19.456&long=405.56&cpuTime=44")
urls.append("http://127.0.0.1:5000/fog/add/?id=3&lat=9.256&long=45.56&cpuTime=54")
urls.append("http://127.0.0.1:5000/device/add/?id=1&lat=92.456&long=14.56&cpuTime=12")
urls.append("http://127.0.0.1:5000/device/add/?id=2&lat=9.356&long=40.56&cpuTime=10")
urls.append("http://127.0.0.1:5000/device/add/?id=3&lat=3.456&long=45&cpuTime=50")
urls.append("http://127.0.0.1:5000/device/add/?id=4&lat=92.456&long=14.56&cpuTime=12")
urls.append("http://127.0.0.1:5000/device/add/?id=5&lat=9.356&long=40.56&cpuTime=10")
urls.append("http://127.0.0.1:5000/device/add/?id=6&lat=3.456&long=45&cpuTime=50")
[requests.get(url) for url in urls]