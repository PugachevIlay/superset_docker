FROM apache/superset:2.0.0

COPY init_superset.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/init_superset.sh

CMD ["init_superset.sh"]