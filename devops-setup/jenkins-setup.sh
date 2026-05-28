

sudo dnf install java-17-openjdk -y


sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo


sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key


sudo yum install jenkins -y


sudo systemctl start jenkins

sudo systemctl enable jenkins


sudo cat /var/lib/jenkins/secrets/initialAdminPassword



