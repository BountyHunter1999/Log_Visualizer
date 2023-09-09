FROM elasticsearch:8.9.2
# FROM elasticsearch:7.13.3

COPY elasticsearch.yml /usr/share/elasticsearch/config/

RUN bin/elasticsearch-plugin install analysis-icu