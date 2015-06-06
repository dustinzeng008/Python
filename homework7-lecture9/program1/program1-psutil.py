from wsgiref.simple_server import make_server
import psutil
import datetime


def psutil_app(environ, start_response):
    systemInfoList = []
    message = ""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)

    boot_time = datetime.datetime.fromtimestamp(
        psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    systemInfoList.append(("BOOT TIME", boot_time))

    cpu_util = psutil.cpu_percent(interval=1, percpu=True)

    i = 1
    cpuInfo = ""
    cpuInfo += "<table width='100%''>"
    for cpu in cpu_util:
        cpuInfo += "<tr>"
        cpuInfo = cpuInfo + "<td>CPU " + str(i) + "</td>"
        cpuInfo = cpuInfo + "<td bgcolor='#FFAEB9'>" + str(cpu) + "%</td></tr>"
        i += 1
    cpuInfo += "</table>"
    systemInfoList.append(("CPU UTILIZATION", cpuInfo))

    mem = psutil.virtual_memory()
    THRESHOLD = 100 * 1024 * 1024  # 100MB
    systemInfoList.append(("AVAILABLE MEMORY", str(mem.available)))
    systemInfoList.append(("USED MEMORY", str(mem.used)))
    systemInfoList.append(("USED PERCENTAGE", str(mem.percent)))

    message += "<table width='50%''>"
    for i in range(len(systemInfoList)):
        if(i % 2 == 0):
            message += "<tr bgcolor='#FFDEAD'>"
        else:
            message += "<tr>"
        message = message + "<td>" + systemInfoList[i][0] + "</td>"
        message = message + "<td>" + systemInfoList[i][1] + "</td></tr>"
    message += "</table>"
    return[bytes(message, 'utf-8')]

httpd = make_server('', 8000, psutil_app)
print("Serving on port 8000...")
httpd.serve_forever()
