

def start_service():
    from jnius import autoclass, cast

    print("1 - start_service")
    mActivity = autoclass("org.kivy.android.PythonActivity").mActivity
    try:
        msg_service = autoclass("org.jupieter.ragaly_news.RagalyBroadcastService")
        try:
            msg_service.start(mActivity)
        except:
            print("NO   msg_service.start")
    except:
        print("NO   RagalyBroadcastService")

    service = autoclass("org.jupieter.ragaly_news.ServiceRagaly")
    service.start(mActivity, "")
    print("3 - end_service")

    return service


if __name__ == '__main__':
    start_service()
    


