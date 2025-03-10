#!/bin/bash

# 获取当前时间作为提交信息
current_time=$(date "+%Y-%m-%d %H:%M:%S")

# 添加所有更改
git add .

# 提交更改
git commit -m "Auto commit at ${current_time}"

# 推送到远程仓库
git push

echo "Changes committed and pushed successfully!"