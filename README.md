
1. `docker run --name redis -p 6379:6379 -d redis`
2. `docker run --name pdf_gen -p 7500:7500 openlabs/docker-wkhtmltopdf-aas`
3. `python app/manage.py rqworker default`
4. `python manage.py runserver`
5. `python manage.py runserver`