# Use official Jenkins LTS image
FROM jenkins/jenkins:lts

# Switch to root user
USER root

# Install required tools
RUN apt-get update && \
    apt-get install -y \
    docker.io \
    git \
    curl \
    unzip && \
    apt-get clean

# Add Jenkins user to docker group
RUN usermod -aG docker jenkins

# Switch back to Jenkins user
USER jenkins

# Expose Jenkins port
EXPOSE 8080

# Default command
CMD ["jenkins.sh"]
