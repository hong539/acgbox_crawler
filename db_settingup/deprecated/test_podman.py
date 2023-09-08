import subprocess

# 執行podman-compose啟動MySQL容器
subprocess.run(['podman-compose', 'up', '-d'])

# 檢查MySQL容器是否正在運行
result = subprocess.run(['podman', 'ps', '-a', '--format', '{{.Names}} {{.Status}}'], capture_output=True)
output = result.stdout.decode('utf-8')
if 'mysql_db_1' in output and 'Up' in output:
    print('MySQL container is running')
else:
    print('MySQL container is not running')

# 停止MySQL容器
subprocess.run(['podman-compose', 'down'])