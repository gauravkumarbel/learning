# Use lightweight nginx to serve the static site
FROM nginx:alpine

# Copy your website file into nginx's default serve directory
COPY dosto_ka_adda.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start nginx (default CMD from base image — no need to override)
