FROM logstash:8.9.2

COPY logstash_simple.conf /etc/logstash/logstash_simple.conf 
COPY logstash.yaml /usr/share/logstash/config/logstash.yml

RUN bin/logstash -f /etc/logstash/logstash_simple.conf 