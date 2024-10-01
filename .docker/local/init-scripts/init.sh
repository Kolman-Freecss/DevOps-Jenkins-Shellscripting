#!/bin/bash

# Create UpdateCenter file with the correct URL (mirror server) (https://get.jenkins.io/plugins/ant/497.v94e7d9fffa_b_9/ant.hpi?mirrorlist)
cat <<EOF > /var/jenkins_home/hudson.model.UpdateCenter.xml
<?xml version='1.0' encoding='UTF-8'?>
<sites>
  <site>
    <id>default</id>
    <url>https://ftp.belnet.be/mirror/jenkins/updates/update-center.json</url>
  </site>
</sites>
EOF
