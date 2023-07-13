import json
import os
import git
import shutil
import C
from RepoParser import RepoParser


class Repo():

    def __init__(self, url: str, username=None, password=None):
        name = os.path.splitext(os.path.basename(url))[0]
        path = f'{C.WORKSPACE_PATH}/{name}'
        self.path = path
        if os.path.exists(path):
            repo = git.Repo(path)
            print('获取本地仓库', repo)
            # 执行git fetch以获取更新
            repo.git.fetch(prune=True)  # 防止被远程删掉的分支还可看到
        else:
            print(f'克隆远程仓库: url={url}')
            try:
                remote_url = url.split('//', 1)
                remote_url = f'{remote_url[0]}//{username}:{password}@{remote_url[1]}'
                repo = git.Repo.clone_from(remote_url, path)
            except:
                print(f'克隆远程仓库异常: url={url}')
            print(f'clone {url}  to {path}')
        self.repo = repo

    def branch(self) -> list[str]:
        """
        列出分支列表
        :return:
        """
        return [b.name for b in self.repo.remote().refs]

    def checkout(self, branch):
        """
        切换分支
        :param branch:
        :return:
        """
        self.repo.git.checkout(branch)

    def clean(self):
        """
        清空仓库
        :return:
        """
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
        pass

    def parse(self):
        """
        解析项目
        :return:
        """
        return RepoParser(self.path)

    def info(self):
        return self.parse()


if __name__ == '__main__':
    # repo = Repo('https://github.com/puppyify/puppyify.git')
    repo = Repo('https://git.psoho.cn/demos/demo-spring-boot.git')
    print(repo.path)
    print(repo.branch())

    # 拉取指定分支
    repo.checkout('origin/develop')

    p = repo.parse()
    print(p)

    print(p.projects)
    if p.isMaven():
        print('Maven')
        p.mavenInfo()
    print()
