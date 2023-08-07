FROM alpine
LABEL org.opencontainers.image.source https://github.com/seboknt/productivityCheck
RUN apk add nginx php
RUN mkdir -p /run/nginx
RUN touch /run/nginx/nginx.pid
RUN adduser -D -g 'www' www
RUN mkdir /www 
RUN chown -R www:www /var/lib/nginx
RUN chown -R www:www /www
COPY nginx.conf /etc/nginx/nginx.conf
COPY www /www
CMD ["php", "-D", "&"]
CMD ["nginx", "-g", "daemon off;"]