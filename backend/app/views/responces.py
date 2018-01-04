class Resp:
    OK = "ok"
    ERROR = "error"

    @staticmethod
    def create(status, **data):
        data.update(status=status)
        return data

    @staticmethod
    def ok(**kwargs):
        return Resp.create(Resp.OK, **kwargs)

    @staticmethod
    def error(errors):
        return Resp.create(
            Resp.ERROR,
            errors=errors
        )
