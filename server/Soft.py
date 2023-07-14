import os

import C
import requests, tarfile
import subprocess


class Soft():

    def __init__(self):
        self.jdk_home = f'{C.SOFT_PATH}/jdk/jdk1.8.0_361'
        self.maven_home = f'{C.SOFT_PATH}/maven/apache-maven-3.8.1'
        pass

    def download(self, name, url):
        output_filename = f'{C.SOFT_PATH}/{name}/{os.path.basename(url)}'
        output_folder = os.path.dirname(output_filename)
        C.mkdirs(output_folder)
        print(f'下载{name}')
        response = requests.get(url)
        response.raise_for_status()
        with open(output_filename, 'wb') as f:
            f.write(response.content)
        print(f'下载{name}完成')

        # 解压
        print(f'解压{name}')
        with tarfile.open(output_filename, 'r:gz') as tar:
            tar.extractall(output_folder)
        print(f'解压{name}完成')

    def install_maven(self):
        if not os.path.exists(self.maven_home):
            url = 'http://127.0.0.1:8080/apache-maven-3.8.1-bin.tar.gz'
            self.download('maven', url)

    def install_jdk(self):
        if not os.path.exists(self.jdk_home):
            url = 'http://127.0.0.1:8080/jdk-8u361-linux-x64.tar.gz'
            self.download('jdk', url)


class Executor():

    def bash(self, command='date'):

        # 加载maven配置
        # Shell命令
        # command = 'mvn clean'

#         command = '''export JAVA_HOME=/var/puppyify/soft/jdk/jdk1.8.0_362
# echo "xxxxxxxx"
# echo "xxxx"
# mvn clean
# for i in `seq 1 100`
# do
#     echo `date` $i
#     sleep 1
# done
#         '''

        # 环境变量PATH
        soft = Soft()
        JAVA_HOME = soft.jdk_home
        MAVEN_HOME = soft.maven_home
        DEFAULT_PATH = '/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
        custom_path = [DEFAULT_PATH, f'{JAVA_HOME}/bin', f'{MAVEN_HOME}/bin']
        custom_env = {
            'JAVA_HOME': JAVA_HOME,
            'MAVEN_HOME': MAVEN_HOME,
            'PATH': ':'.join(custom_path)
        }

        print(custom_env)

        # 指定目录
        output_file = f'{C.LOGS_PATH}/output.log'

        with open(output_file, 'w') as f:
            # 执行Shell命令
            process = subprocess.Popen(command, shell=True,
                                       env=custom_env,
                                       cwd=f'{C.WORKSPACE_PATH}/demo-spring-boot',
                                       stdout=f, stderr=subprocess.STDOUT
                                       )
            # process.communicate()

        print('执行成功')
        #
        # # 获取命令执行的返回值
        # return_code = process.returncode
        #
        # if return_code == 0:
        #     print('命令执行成功')
        # else:
        #     print(f'命令执行失败，返回码: {return_code}')
        # ...


if __name__ == '__main__':
    # Soft().install_jdk()
    # print(Soft().install_maven())
    print(Executor().bash())
