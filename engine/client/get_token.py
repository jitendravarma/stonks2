import time

from urllib import parse

from selenium import webdriver

from get_access_token import GetPass


def get_driver():
    chromedriver_path = '/opt/homebrew/bin/chromedriver'
    brave_path = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    option = webdriver.ChromeOptions()
    option.add_argument("user-data-dir=selenium")
    option.binary_location = brave_path
    return webdriver.Chrome(executable_path=chromedriver_path, options=option)


def get_token():
    browser = get_driver()
    try:
        browser.get("https://api.fyers.in/api/v2/generate-authcode?client_id=LSCTXIM2YP-100&redirect_uri=https%3A%2F%2Fwww.fasterthanlight.in%2F&response_type=code&state=state&scope=&nonce=")
        time.sleep(5)
        url = browser.current_url
        query_def = parse.parse_qs(parse.urlparse(url).query)
        auth_code = query_def['auth_code'][0]
        get_pass = GetPass()
        get_pass.auth_token = auth_code
        _, response = get_pass.call()
        print(response['access_token'])
        browser.close()
        return response['access_token']
    except Exception as error:
        print(error)
        browser.close()


def main():
    get_token()


if __name__ == '__main__':
    main()
