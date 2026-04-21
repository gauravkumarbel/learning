#!/bin/bash
echo please wait 10 minutes system update!
sudo dnf update
echo sucssefully system update
echo please wait java-jdk installing
sudo dnf install java-25-openjdk-devel -y
echo java-jdk install
echo please wait 2 minute jenkins download and insttaing!  
sudo wget -O /etc/yum.repos.d/jenkins.repo \
https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2025.key sudo dnf upgrade
sudo dnf install jenkins
sudo systemctl daemon-reload
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd –reload
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
http://localhost://8080

