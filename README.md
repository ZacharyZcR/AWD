# AWD

2019 年写的 AWD 攻防赛工具，包含目标配置、比赛脚本和文件防护。代码保留在这里，给那段边学边写的日子留个纪念。

## 目录

| 路径 | 内容 | 状态 |
| --- | --- | --- |
| `AWD_Auto_Attack_Framework/` | 最初的攻击侧脚本 | Python 2 历史代码 |
| `AWD_Auto_Defend_Framework/` | 最初的防御侧脚本和 PHP 日志 | Python 2 历史代码 |
| `Extend_Module/` | 流量混淆实验 | 历史代码 |
| `awdphpspear/` | 后续模块化版本 | 文件、HTTP 请求、文件监控模块已整理为 Python 3 |

原始脚本和 Word 文档保留作参考。`awdphpspear` 中的 `attack.py`、`shell.py`、`upload.py`、`tools.py` 和旧 `setup.py` 仍是历史版本，不作为 Python 3 入口。

## 整理后的模块

使用 Python 3.10+，在仓库根目录运行：

```sh
python3 -m pip install -r requirements.txt
python3 -m awdphpspear.protect --help
```

文件防护：

```sh
# 创建备份；目标已存在时直接报错，不覆盖旧备份
python3 -m awdphpspear.protect backup /path/to/site --backup /path/to/site-backup

# 持续报告相对于启动时的新增、删除和修改，Ctrl+C 结束
python3 -m awdphpspear.protect check /path/to/site

# 以备份为基准恢复文件；新增内容会被移除
python3 -m awdphpspear.protect restore /path/to/site --backup /path/to/site-backup
```

不指定 `--backup` 时，默认使用源目录旁的 `<目录名>.awd-backup`。恢复模式若没有备份，会先备份当前目录；已有备份则作为恢复基准。备份目录与源目录不能互相包含，符号链接会明确报错。监控包括 `.txt` 文件和空目录。

恢复采用轮询，适用于静态目录；它会撤销运行期间产生的合法变更。备份和扫描不提供并发写入下的一致性快照，请先准备好所需基准。

文件和 HTTP 帮助函数显式导入：

```python
from awdphpspear.files import read_array
from awdphpspear.request import post_json
```

文件函数返回数据，不再打印文件内容。HTTP 函数返回 `requests.Response`，默认超时为 10 秒，连接失败和 HTTP 错误直接抛出异常；`post_json` 使用 JSON 编码。

此次整理移除了包导入时的通配导入。旧菜单、批量 PHP 日志注入和备份删除接口留在历史代码中，不接入新的防护入口。

## 验证

```sh
python3 -m unittest discover -s tests
```

## License

MIT，见 [LICENSE](LICENSE)。
