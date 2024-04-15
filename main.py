from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def __get_htmal_content(self):
        """ Метод для получения содержимого html-файла"""

        with open("index.html") as file:
            return file.read()

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """

        query_components = parse_qs(urlparse(self.path).query)  # Получение параметров запроса
        print(query_components)  # Вывод параметров запроса в консоль
        page_content = self.__get_htmal_content()  # Получение содержимого html-файла
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)  # Инициализация веб-сервера
    print("Server started http://%s:%s" % (hostName, serverPort))  # Вывод сообщения о запуске сервера

    try:
        webServer.serve_forever()  # Запуск сервера
    except KeyboardInterrupt:
        pass
    webServer.server_close()  # Остановка сервера
    print("Server stopped.")  # Вывод сообщения об остановке сервера
