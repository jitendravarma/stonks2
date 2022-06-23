import requests

cookies = {
    'NSE-TEST-1': '1960845322.20480.0000',
    'JSESSIONID': 'B8104DC1B1C874A9A892F6300BC833EE.tomcat2',
    'bm_mi': '3A0CE1C67D60D28314C084FD3D085027~YAAQ1SdzaKhz23OBAQAASZVWhxBlUFB4NWcV+F2wPZV8klRXlLStgC5Nguu/H5sraR4xW7sgmidTtYv8q28S8HwegfCsnWjR89av49oWB34EQiLjvlyEfOrQMM5MNbYKpHFC6JxvRgJM29eJCiCuhcEZcCbwU8nij9yugljr/L8sQpV7rfibeAWu1ATLOPplQg68GNbdaLxc0mCvE9vGCegG06raOwQ9YYsFlVbgeoa95Q9osJGxSgau+eUWoVB27SEanIRStjIvDD3DQyvkTpZvIVRx6wQLvdAbCO3kpYYn2R7wPSdtD7Ifi/VN8l26kprJ8MlIryzMsnNqPpAenyaeO/jYBpgN~1',
    'ak_bmsc': '0FCF9489714EC53DCE3DC9EA674BBE74~000000000000000000000000000000~YAAQ1SdzaLxz23OBAQAA4JdWhxDjHifT+bAZW6rYRZgz2gJPduvg3FYs1vAMRWAcVexV5OTN1EKLYok6CgrXNFJjh2ew5eymYCje4v+a4upirH9sQzCtYl4m+04/aIBIfih/FvmV8g4ouXWlCBNco2u009L1vnPUwEz+P+/JZpjJ+Urzq77EaSrWphuriwyRM5on6os53xRpFb2sJy7lrx2ekHPxYNDE6PnpP1jW8X3IRJcFtbmn+1CX71CliwVQddHzc5r7VgwL6pnENu9q5g1O/mIUypWaOXoZEa7JJL5+eAXf+l+O06qANmWgpFQ/JXnFSOea5uD8SwmgbDLBI1IRh5s2dFLS9+/CyFyBqIV4WK7CwAahIoBX/D5negHCgB25n+11s3ihEAdPbrRcL1EWB/1Bc6kpZJmpNRscUFtfn6Vo2p9hZjGPDSK877QHkN7FKA2ibKvZ7XdQyDnkr7xafdzc/LKit7INZzNO2Z8lKpKM63au5OsyUo2YqMRAQp0C5LKcrIUuCo7WETAtje76c0s=',
    'bm_sv': '8CC80EE865DC2D437E46C639F0B9FC04~YAAQ1SdzaEWh23OBAQAAzC1bhxA9mVoYaY40/hhf7y16OMsQsFuNCl8/YtNkw/cEpgfOGYJ7roSqcy1Gb0IDpDu/Y+h2f4QTj/HCYjh2ItYlNOQx4oVOqlzbjMvDQ91nhN2rn2Gr3xqMbRhrQpQM+56buUjiGdcAnCSp2l0gI/kaODxbueSDGUFEWY7hWi/3pvknt8wPlAIL5kCVhiOJaQgS0cTWw2tuztwqnGwd7U9oaJsQqfsqhk8DVRaHtat9bE/b~1',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-GB;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'NSE-TEST-1=1960845322.20480.0000; JSESSIONID=B8104DC1B1C874A9A892F6300BC833EE.tomcat2; bm_mi=3A0CE1C67D60D28314C084FD3D085027~YAAQ1SdzaKhz23OBAQAASZVWhxBlUFB4NWcV+F2wPZV8klRXlLStgC5Nguu/H5sraR4xW7sgmidTtYv8q28S8HwegfCsnWjR89av49oWB34EQiLjvlyEfOrQMM5MNbYKpHFC6JxvRgJM29eJCiCuhcEZcCbwU8nij9yugljr/L8sQpV7rfibeAWu1ATLOPplQg68GNbdaLxc0mCvE9vGCegG06raOwQ9YYsFlVbgeoa95Q9osJGxSgau+eUWoVB27SEanIRStjIvDD3DQyvkTpZvIVRx6wQLvdAbCO3kpYYn2R7wPSdtD7Ifi/VN8l26kprJ8MlIryzMsnNqPpAenyaeO/jYBpgN~1; ak_bmsc=0FCF9489714EC53DCE3DC9EA674BBE74~000000000000000000000000000000~YAAQ1SdzaLxz23OBAQAA4JdWhxDjHifT+bAZW6rYRZgz2gJPduvg3FYs1vAMRWAcVexV5OTN1EKLYok6CgrXNFJjh2ew5eymYCje4v+a4upirH9sQzCtYl4m+04/aIBIfih/FvmV8g4ouXWlCBNco2u009L1vnPUwEz+P+/JZpjJ+Urzq77EaSrWphuriwyRM5on6os53xRpFb2sJy7lrx2ekHPxYNDE6PnpP1jW8X3IRJcFtbmn+1CX71CliwVQddHzc5r7VgwL6pnENu9q5g1O/mIUypWaOXoZEa7JJL5+eAXf+l+O06qANmWgpFQ/JXnFSOea5uD8SwmgbDLBI1IRh5s2dFLS9+/CyFyBqIV4WK7CwAahIoBX/D5negHCgB25n+11s3ihEAdPbrRcL1EWB/1Bc6kpZJmpNRscUFtfn6Vo2p9hZjGPDSK877QHkN7FKA2ibKvZ7XdQyDnkr7xafdzc/LKit7INZzNO2Z8lKpKM63au5OsyUo2YqMRAQp0C5LKcrIUuCo7WETAtje76c0s=; bm_sv=8CC80EE865DC2D437E46C639F0B9FC04~YAAQ1SdzaEWh23OBAQAAzC1bhxA9mVoYaY40/hhf7y16OMsQsFuNCl8/YtNkw/cEpgfOGYJ7roSqcy1Gb0IDpDu/Y+h2f4QTj/HCYjh2ItYlNOQx4oVOqlzbjMvDQ91nhN2rn2Gr3xqMbRhrQpQM+56buUjiGdcAnCSp2l0gI/kaODxbueSDGUFEWY7hWi/3pvknt8wPlAIL5kCVhiOJaQgS0cTWw2tuztwqnGwd7U9oaJsQqfsqhk8DVRaHtat9bE/b~1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
}

params = {
    'indexType': 'NIFTY 50',
    'fromDate': '14-06-2022',
    'toDate': '22-06-2022',
}

response = requests.get('https://www1.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp',
                        params=params, cookies=cookies, headers=headers)

print(response.text)
