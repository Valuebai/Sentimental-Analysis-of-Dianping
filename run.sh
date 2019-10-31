
nohup gunicorn -w 4 -b 0.0.0.0:8688 run:app > gunicorn.log 2>&1 &
