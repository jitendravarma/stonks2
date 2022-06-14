from fyers_api import accessToken

from fyers_api import fyersModel


class Scutum(object):

    def __init__(self):
        self.app_id = "L3OO6RQXHO"
        self.app_secret = "YUX01K3S7V"
        # self.token = self.get_token()

    def get_token(self):
        print('get token called')
        app_session = accessToken.SessionModel(self.app_id, self.app_secret)
        response = app_session.auth()
        if response['code'] == 200:
            auth_code = response['data']['authorization_code']
            app_session.set_token(auth_code)
            print(app_session.generate_token())
            return response['data']['authorization_code']
        return None

    def get_scuti(self, is_async=False):
        return True

    def get_profile(self, is_async=False):
        fyers = fyersModel.FyersModel(is_async)
        return fyers.get_profile(
            token="gAAAAABgpU5go_1W1lBTexof8euwsSTj0kwT4Wkb51RJ4mANzEibgmmUlN2w-KjGZg46aBPS1FMb2VkR2Y-KM0vvM3-1ZYwMLezzyWNECJQAVRXwErS71S4")
# https://fasterthanlight.in/?access_token=gAAAAABf13zuMNFfpbuJ7CDJtPOEuviBY7O4icFEXfoYyZUkLMaoOPDzkX3344viFFUiu-qmpii74Bq1Jbcc6eT5r2kDP9YgvKnnYIk_18oYmhPnwyi7wK8=&user_id=XA00298&poa_flag=N


if __name__ == "__main__":
    scuti = Scutum()
    print(scuti.get_profile(False))
