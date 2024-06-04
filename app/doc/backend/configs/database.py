defaultDriver = 'sqlite'  # 数据库类型
sqlite = {
    'connect': 'default',  # 默认链接
    'default': {
        # 相对于应用resources目录
        'database': 'demo.db',
        'pragmas': {
            'journal_mode': 'wal',
            'cache_size': 10000,  # 10000 pages, or ~40MB 以kib为单位设置页面缓存大小
            'foreign_keys': 1,  # 强制外键约束
            'ignore_check_constraints': 0,  # 强制检查约束
            'synchronous': 0,  # 让操作系统处理fsync（小心使用）
        }
    },
}
mysql = {
    'connect': 'default',  # 默认链接
    'default': {
        'database': 'demo',
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'port': 3306,
        'charset': 'utf8mb4'
    }
}

postgresql = {
    'connect': 'default',  # 默认链接
    'default': {
        'database': 'test',
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'port': 5432,
    }
}
