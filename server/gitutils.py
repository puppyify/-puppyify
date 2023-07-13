import os
import git
import shutil

WORKSPACE_PATH = '../workspace'


class Repo():

    def __init__(self, url, branch='master'):
        name = os.path.splitext(os.path.basename(url))[0]
        path = f'{WORKSPACE_PATH}/{name}'
        self._path = path
        print(f'初始化仓库: url={url}')
        if os.path.exists(path):
            repo = git.Repo(path)
            print('获取仓库', repo)
            # 执行git fetch以获取更新
            repo.git.fetch(prune=True)  # 防止被远程删掉的分支还可看到
        else:
            try:
                repo = git.Repo.clone_from(url, path, branch=branch)
            except:
                print(f'克隆仓库异常: url={url}, branch={branch}')
                print(f'使用默认分支克隆仓库: url={url}')
                repo = git.Repo.clone_from(url, path)
            print(f'clone {url}  {branch} to {path}')
        self._repo = repo

    def branchs(self) -> list[str]:
        """
        列出分支列表
        :return:
        """
        return [b.name for b in self._repo.remote().refs]

    def checkout(self, branch):
        """
        切换分支
        :param branch:
        :return:
        """
        self._repo.git.checkout(branch)

    def clean(self):
        """
        清空仓库
        :return:
        """
        if os.path.exists(self._path):
            shutil.rmtree(self._path)
        pass


if __name__ == '__main__':
    # repo = Repo('https://github.com/puppyify/puppyify.git')
    repo = Repo('https://git.psoho.cn/demos/demo-spring-boot.git', 'mss')
    print(repo.branchs())
