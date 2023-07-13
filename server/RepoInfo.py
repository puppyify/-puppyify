import os
from collections import defaultdict


class RepoInfo(dict):

    def __init__(self, directory):
        # 目录路径

        # 存储每种语言类型的文件数量
        language_counts = defaultdict(int)
        project_counts = defaultdict(int)

        # 文件扩展名与语言类型的映射关系
        language_mapping = {
            'py': 'python',
            'java': 'java',
            'cpp': 'c++',
            'js': 'js',
            'vue': 'vue',
            # 添加其他语言类型的映射关系
        }

        # 项目
        project_mapping = {
            'pom.xml': 'maven',
            'package.json': 'node'
        }

        # 遍历目录及其子目录中的文件
        for root, dirs, files in os.walk(directory):
            for filename in files:
                _, ext = os.path.splitext(filename)
                ext = ext.lstrip('.')  # 去除扩展名中的点号

                # 判断文件的语言类型
                if ext in language_mapping:
                    language_type = language_mapping[ext]
                    language_counts[language_type] += 1

                if filename in project_mapping:
                    project_counts[project_mapping[filename]] += 1

        # 计算每种语言类型的占比
        total_files = sum(language_counts.values())
        languages = [
            {'type': language_type, 'percent': f'{count / total_files * 100 :.2f}'} for language_type, count in
            language_counts.items()
        ]
        languages = sorted(languages, key=lambda x: float(x['percent']), reverse=True)
        self.languages = languages
        self.language_type = self.languages[0]['type'] if len(self.languages) >= 1 and self.languages[0][
            'type'] else None

        # 计算项目信息
        total_project_files = sum(project_counts.values())
        projects = [
            {'type': language_type, 'percent': f'{count / total_project_files * 100 :.2f}'} for language_type, count in
            project_counts.items()
        ]
        projects = sorted(projects, key=lambda x: float(x['percent']), reverse=True)
        self.projects = projects
        self.project_type = self.projects[0]['type'] if len(self.projects) >= 1 and self.projects[0]['type'] else None

        dict.__init__(self, languages=languages, projects=projects, project_type=self.project_type,
                      language_type=self.language_type)

    def isMaven(self):
        return self.project_type == 'maven'
