FROM nginx:alpine

COPY vent-app.zip /
COPY ./default.conf /etc/nginx/conf.d/
RUN unzip vent-app.zip
RUN cp -r vent-app/* /usr/share/nginx/html/
RUN rm -rf vent-app*
