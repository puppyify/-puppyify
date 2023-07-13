

## 切换分支


```bash
Started by user 维新
Running as SYSTEM
Building in workspace /var/lib/jenkins/workspace/gray-gupaoedu-api
The recommended git tool is: NONE
using credential 7481b24a-e44d-4f1c-b2c0-8eb02795e840
 > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/gray-gupaoedu-api/.git # timeout=10
Fetching changes from the remote Git repository
 > git config remote.origin.url https://git.gupaoedu.cn/gp-private-ke/gupaoedu-ke-server.git # timeout=10
Fetching upstream changes from https://git.gupaoedu.cn/gp-private-ke/gupaoedu-ke-server.git
 > git --version # timeout=10
 > git --version # 'git version 1.8.3.1'
using GIT_ASKPASS to set credentials webhook
 > git fetch --tags --progress https://git.gupaoedu.cn/gp-private-ke/gupaoedu-ke-server.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/v_scrm^{commit} # timeout=10
Checking out Revision 9a9bb7f4f14f8c3e60e57802fc3b4653a898a6a7 (refs/remotes/origin/v_scrm)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 9a9bb7f4f14f8c3e60e57802fc3b4653a898a6a7 # timeout=10
Commit message: "Merge remote-tracking branch 'origin/v_scrm' into v_scrm"
 > git rev-list --no-walk 9a9bb7f4f14f8c3e60e57802fc3b4653a898a6a7 # timeout=10
[gray-gupaoedu-api] $ /bin/sh -xe /tmp/jenkins5700837839169183358.sh
+ mvn -T 1C clean package -pl gponline-web -am -Dmaven.test.skip=true -P gray
[INFO] Scanning for projects...
[WARNING] 
[WARNING] Some problems were encountered while building the effective model for com.gponline:gponline-mfw:jar:2.0.0-SNAPSHOT
[WARNING] 'dependencyManagement.dependencies.dependency.(groupId:artifactId:type:classifier)' must be unique: com.aliyun:aliyun-java-sdk-sts:jar -> duplicate declaration of version 3.0.0 @ com.gponline:gponline:2.0.0-SNAPSHOT, /var/lib/jenkins/workspace/gray-gupaoedu-api/pom.xml, line 271, column 25
```

### 无法签出代码

```bash
git clone https://myname:mypassword@x.x.x/x/x.git
```

## maven构建

```bash
mvn -T 1C clean package -Dmaven.test.skip=true
```

