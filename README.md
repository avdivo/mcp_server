# MCP server

GitHub: [https://github.com/avdivo/mcp_server](https://github.com/avdivo/mcp_server)  

## Описание
Локальный MCP сервер для получения моделью ИИ информации.  
Выступает посредником между клиентом чата с моделью ИИ и сервисами предоставляющими услуги в интернете.  
Разворачивается на локальном компьютере.

## Функции
- предоставление информации о погоде в указанном городе
- новостей за последнюю неделю
- курса доллара на сегодня

## Использование
После установки и настройки сервера на компьютере и подключения его клиенту ИИ, в чате 
искусственному интеллекту можно задавать вопросы, ответов на которые он изначально не знает.
Для получения информации для ответов на эти вопросы, клиент воспользуется сервером, 
и сможет вернуть пользователю адекватные ответы.

## Структура проекта

```plaintext
├── mcp_server/                       # Основной каталог проекта
│   ├── .venv/                        # Виртуальное окружение
│   ├── services/                     # Логика сервисов
│   │   ├── currency_service.py       # Сервис валют
│   │   ├── news_service.py           # Сервис новостей
│   │   ├── weather_service.py        # Сервис погоды
│   ├── .env                          # Файл окружения
│   ├── .gitignore                    # Файл игнорирования Git
│   ├── .python-version               # Версия Python
│   ├── local_server.py               # Локальный сервер
│   ├── mcp.json                      # Конфигурационный файл MCP
│   ├── pyproject.toml                # Файл конфигурации проекта
│   ├── README.md                     # Файл описания проекта
│   ├── uv.lock                       # Файл блокировки зависимости
```

## Используемые зависимости
mcp[cli]
httpx
requests
python-dotenv
newsapi-python


## Файл .env
ACCUWEATHER_API_KEY=<токен для сервера погоды>  
NEWS_API_KEY=<токен для сервера новостей>  
NEWS_API_BASE_URL=https://newsapi.org/v2 (базовый API новостного сервера)  
CBR_API_URL=https://www.cbr.ru/scripts/XML_daily.asp (url для получения курса доллара)

> Файл нужно поместить в корень проекта, папку 'mcp_server'.

## Установка и запуск
1. Открыть терминал.
2. Перейти в папку, где будет установлен сервер.
3. Клонировать репозиторий:
    ```bash
    git clone https://github.com/avdivo/mcp_server
    ```
4. Перейти в папку проекта.
    ```bash
    cd mcp_server/
    ```
   > Не забыть поместить или создать в папке файл .env
5. Установить uv
    ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source ~/.bashrc
    ```
   Если curl не установлен
   ```bash
   sudo apt update
   sudo apt install curl
    ```
6. Установить зависимости
   ```bash
   uv sync
   ```
7. Для проверки работы серера можно запустить его
   ```bash
   uv run local_server.py
   ```
8. Для остановки
   ```bash
   CTRL + C
   ```
   
## Добавить настройки сервера MCP в конфигурационный файл клиента
1. Для Claude Desktop
- MacOS: ~/Library/Application Support/Claude/claude_desktop_config.json
- Windows: %APPDATA%/Claude/claude_desktop_config.json
- Linux: ~/.config/Claude/claude_desktop_config.json

2. Для Cursor
Linux: ~/.config/Cursor/mcp.json

```json
{
    "mcpServers": { 
      "info-services": {
        "command": "uv",
        "args": [
          "--directory",
          "/home/<путь к папке сервера>/mcp_server",
          "run",
          "local_server.py"
        ],
        "cwd": "/home/<путь к папке сервера>/mcp_server",
        "env": {
          "PYTHONPATH": "/home/<путь к папке сервера>/mcp_server"
        }
      }
    }
  }
```