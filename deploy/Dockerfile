# Build the checked HTML first using the commands in README.md.
FROM nginxinc/nginx-unprivileged:stable-alpine@sha256:f5116ed4606f3eb015dd4a8e28cb9b351476dc0ad4bc6e9f93b19cec130cdf03
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY _build/html/ /usr/share/nginx/html/python-phd/
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
