class Resp:
    OK = "ok"

    @staticmethod
    def create(status, **data):
        data.update(status=status)
        return data

    @staticmethod
    def ok():
        return Resp.create(Resp.OK)
