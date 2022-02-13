# Решение тестового задания для разработчика на python - 
## Разработка микросервиса (обработка заказов, печать чеков)

Подробнее об условиях можно [посмотреть тут](https://github.com/smenateam/assignments/blob/master/backend/README.md)


# Development
0. `mv .env.example .env.dev` - .env.dev for docker, .env for local
1. `docker-compose up --build`
2. `docker exec -it app python manage.py loaddata default_data.json` 



### TODO
2. Запилить тесты
3. фикстуры
4. подключить postgres
5. логгирование
