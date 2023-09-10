# Log_Visualizer

This Project used Elasticsearch, Logstash and Kibana to visualize logs in Python in realtime.

![Process Workflow](index.jpeg)

## How to Run?

- `docker-compose up`
- Goto Kibana (http://localhost:5601)
- Analytics Discover, put the settings as follows ![Initial setup](./setting_index.png)
- **Boom** done

## Sample graphs

- Bar Graph ![Bar Graph](./Graphs/sample_visualization.png)
- Line graph ![Line Graph](./Graphs/line_graph.png)
- Heat Map ![Heat Map](./Graphs/heat-map.png)
- Donut graph ![Donut Graph](./Graphs/donut.png)
- Pie graph ![Pie Graph](./Graphs/pie.png)
- Waffle graph ![Waffle Graph](./Graphs/waffle.png)
