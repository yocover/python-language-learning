# python-language-learning
python language learning



Milvus 架构中的三个组件各自扮演不同的角色：
milvus-etcd：
ETCD 是一个分布式键值存储系统
在 Milvus 中负责元数据管理
存储集合结构、分区信息、索引参数等元数据
提供一致性保证，确保数据操作的可靠性
可以理解为 Milvus 的"大脑"，管理系统配置和状态
milvus-minio：
MinIO 是一个高性能的对象存储服务
在 Milvus 中作为向量数据的持久化存储层
存储原始向量数据、索引文件、日志等
提供可靠的文件存储，支持数据备份和恢复
可以理解为 Milvus 的"硬盘"，负责实际数据存储
milvus-standalone：
核心 Milvus 服务，处理向量的存储、索引和检索
提供 API 接口，处理客户端请求
管理向量的增删改查操作
执行 ANN（近似最近邻）搜索算法
协调其他组件，如 etcd 和 MinIO
可以理解为 Milvus 的"计算引擎"，处理核心业务逻辑
这三个组件共同工作：etcd 管理元数据，MinIO 存储数据，Milvus 服务本身处理数据操作和搜索。在 docker-compose 中将它们组合在一起，形成一个完整的 Milvus 向量数据库系统。
此外，配置中还包含了 attu，这是 Milvus 的可视化管理界面，用于监控和管理 Milvus 数据库。

