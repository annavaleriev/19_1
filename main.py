import json
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def __get_htmal_content(self):
        with open("index.html") as file:
            return file.read()

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        if "email" in query_components and "@" not in query_components["email"][0]:
            self.send_response(400)
            page_content = "не верный email"
        else:
            self.send_response(200)  # Отправка кода ответа
            page_content = self.__get_htmal_content()
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа

    def do_DELETE(self):
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(self.data_string)
        print()


        # data = [1, 2, 3, 4]
        # query_components = parse_qs(urlparse(self.path).query)
        # user = query_components.get("user")
        # if user:
        #     user_id = int(user[0])
        #     if user_id in data:
        #         data.remove(user_id)
        #
        # print(data)
        # print()


# if __name__ == "__main__":
#     # Инициализация веб-сервера, который будет по заданным параметрам в сети
#     # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
#     webServer = HTTPServer((hostName, serverPort), MyServer)
#     print("Server started http://%s:%s" % (hostName, serverPort))
#
#     try:
#         # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
#         webServer.serve_forever()
#     except KeyboardInterrupt:
#         # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
#         pass
#
#     # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
#     webServer.server_close()
#     print("Server stopped.")
