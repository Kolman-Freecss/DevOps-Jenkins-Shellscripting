# Use the Jenkins base image
FROM kolmanfreecss/jenkins-git:latest

# Switch to the root user to install packages
USER root

# Copy the shell script into the image
COPY install_deps.sh /usr/local/bin/install_deps.sh

# Execute the shell script
RUN /usr/local/bin/install_deps.sh

# Switch back to the Jenkins user
#USER jenkins