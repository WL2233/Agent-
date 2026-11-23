使用 **uv 安装 FastAPI** 是很好的选择，而且 FastAPI 官方文档现在也推荐使用 uv 管理项目、依赖和虚拟环境。

[FastAPI](https://fastapi.tiangolo.com/zh/#example)

下面以 Windows 11 + PowerShell 为例。

## **一、安装 uv**

**uv 本身不依赖预先安装 Python**，它可以自动下载和管理 Python。如果还没有安装 uv，可以使用 Windows 自带的包管理器：

```
winget install --id astral-sh.uv -e
```

安装完成后，重新打开 PowerShell，检查版本：

```
uv --version
```

## **二、创建 FastAPI 项目**

依次执行：

```
# 1. 创建项目
uv init fastapi-demo --bare

# 2. 进入项目目录
cd fastapi-demo

# 3. 安装 FastAPI（包含标准依赖）
uv add "fastapi[standard]"
```

**uv 会自动创建** `.venv` **虚拟环境**，不需要手动创建或激活。

FastAPI

项目结构大致如下：

```
fastapi-demo/
├── .venv/           # 虚拟环境
├── pyproject.toml    # 项目配置和依赖
└── uv.lock           # 依赖版本锁定
```

## **三、编写并启动 FastAPI**

在项目根目录创建 `main.py`：

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello FastAPI!"}
```

启动开发服务器：

```
uv run fastapi dev main.py
```

打开浏览器：

- [http://127.0.0.1:8000](http://127.0.0.1:8000?utm_source=chatgpt.com)：查看返回结果

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs?utm_source=chatgpt.com)：使用自动生成的接口测试页面

## **四、uv 常用命令**

| 命令                       | 作用                    |
| ------------------------ | --------------------- |
| `uv init`                | 初始化项目                 |
| `uv init 文件名`            | 初始化项目，在当前目录下创建子目录<br> |
| `uv add fastapi`         | 安装并记录依赖               |
| `uv remove fastapi`      | 移除依赖                  |
| `uv sync`                | 根据项目配置同步依赖            |
| `uv run main.py`         | 使用项目环境运行 Python 文件    |
| `uv run fastapi dev`     | 启动 FastAPI 开发服务器      |
| `uv python install 3.12` | 安装指定 Python 版本        |

## **五、如果不想安装 standard 依赖**

可以改成：

```
uv add fastapi uvicorn
```

然后运行：

```
uv run uvicorn main:app --reload
```

这里的 `uvicorn` 是负责运行 FastAPI 应用的服务器。

**我的建议：** 如果你准备长期使用 Python 开发后端服务，采用 `uv init` + `uv add` + `uv run` 这套流程就很好。以后安装其他 Python 库，也都可以交给 uv 管理。

官方文档：[uv 使用指南](https://docs.astral.sh/uv/?utm_source=chatgpt.com)。


### [FastAPI学习示例](https://fastapi.tiangolo.com/zh/#example)

