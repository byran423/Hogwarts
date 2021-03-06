"""HTTP-specific events."""
import mitmproxy.http
from mitmproxy import http


class Events:
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        """
            An HTTP CONNECT request was received. Setting a non 2xx response on
            the flow will return the response to the client abort the
            connection. CONNECT requests and responses do not generate the usual
            HTTP handler events. CONNECT requests are only valid in regular and
            upstream proxy modes.
        """
        pass

    def requestheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
            HTTP request headers were successfully read. At this point, the body
            is empty.
        """
        pass

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        print(flow.request.url)
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json" in flow.request.url:
            with open('/Users/yangbo/Code/Hogwos/mock/xiuqiuhangqing.json', encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    200,
                    f.read(), )

    def responseheaders(self, flow: mitmproxy.http.HTTPFlow):
        """
            HTTP response headers were successfully read. At this point, the body
            is empty.
        """
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """

        pass



    def error(self, flow: mitmproxy.http.HTTPFlow):
        """
            An HTTP error has occurred, e.g. invalid server responses, or
            interrupted connections. This is distinct from a valid server HTTP
            error response, which is simply a response with an HTTP error code.
        """
        pass

addons = [Events()]
if __name__ == '__main__':

    from mitmproxy.tools.main import mitmdump
    # 使用debug模式启动mitmdump
    # __file__指当前文件
    # print(__file__)
    mitmdump(['-p', '8080', '-s', __file__])







