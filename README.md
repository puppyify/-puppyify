# 关于Puppyify

<p>
  <a href="https://github.com/puppyify/puppyify" class="link github-link" target="_blank"><img style="max-width: 100px;" alt="GitHub Repo stars" src="https://img.shields.io/github/stars/puppyify/puppyify?style=social"></a>
  <img alt="csharp" src="https://img.shields.io/badge/language-python-yellow.svg">
  <img alt="csharp" src="https://img.shields.io/badge/language-vue-brightgreen.svg">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-blue.svg">
  <img alt="version" src="https://img.shields.io/badge/version-0.1.0-brightgreen">
</p>

Puppyify是一个持续集成工具，从此告别繁琐的Jenkins。

# 适用场景

使用Puppyify自动化您的开发工作流程，让您可以专注于最重要的工作。Puppyify通常用于:

- 项目构建
- 部署

执行重复的任务，节省时间，并优化您的开发过程。


# 特性

- 开箱即用，无需安装各种插件
- 自动检测项目，生成构建任务
- 支持快速回退到指定版本
- 支持webhook触发

# 如何使用

提供方便的docker镜像

```bash
docker run -it --name puppyify -p 8000:8000 puppyify/puppyify
```

打开浏览器，访问**[http://127.0.0.1:8000](http://127.0.0.1:8000)**，开启轻松、快乐构建之旅。


# 授权协议

Puppyify 使用 **[MIT协议](https://github.com/puppyify/puppyify/blob/master/LICENSE.txt)**，可以放心商用。
