FROM apache/superset:2.0.0

USER root

COPY init_superset.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/init_superset.sh

USER superset

CMD ["init_superset.sh"]