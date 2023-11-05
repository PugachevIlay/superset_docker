#!/bin/bash

# Установите переменную окружения SUPERSET_SECRET_KEY, если она не установлена
if [ -z "$SUPERSET_SECRET_KEY" ]; then
  SUPERSET_SECRET_KEY="qaMnUCm44v7DHmMChzyT1LL9SNuf6Kwx9QFPFWxVQiYZeRSs83UwEbQ7"
fi

# Создайте администратора Superset, если он ещё не существует
superset fab create-admin \
  --username admin \
  --firstname Superset \
  --lastname Admin \
  --email admin@superset.com \
  --password admin

# Обновите базу данных Superset
superset db upgrade

# Инициализируйте Superset
superset init

# Запустите Superset
superset run -h 0.0.0.0 -p 8088