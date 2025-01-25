FROM jenkins/jenkins:lts

# Switch to root user to install plugins
USER root

# Install Jenkins plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# Copy CasC configuration
COPY jenkins.yaml /usr/share/jenkins/ref/jenkins.yaml

# Set CasC configuration path
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/jenkins.yaml

# Switch back to Jenkins user
USER jenkins
