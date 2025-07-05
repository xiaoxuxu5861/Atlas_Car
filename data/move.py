import os
import shutil

# 源目录和目标目录路径
source_dir = r"D:\WorkSpace\Atlas_Car\data"
target_dir = r"D:\WorkSpace\Atlas_Car\data_json"

# 创建目标目录（如果不存在）
os.makedirs(target_dir, exist_ok=True)

# 遍历源目录中的所有文件
for filename in os.listdir(source_dir):
    # 检查是否为JSON文件
    if filename.endswith('.json'):
        # 构建源JSON文件和目标JSON文件的完整路径
        source_json = os.path.join(source_dir, filename)
        target_json = os.path.join(target_dir, filename)
        
        # 移动JSON文件
        shutil.move(source_json, target_json)
        print(f"已移动: {filename}")

print("处理完成！")