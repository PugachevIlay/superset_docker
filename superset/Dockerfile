FROM apache/superset:2.0.0

EXPOSE 8080

ENV SUPERSET_SECRET_KEY="qaMnUCm44v7DHmMChzyT1LL9SNuf6Kwx9QFPFWxVQiYZeRSs83UwEbQ7"

RUN superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin

RUN superset db upgrade

RUN superset init
