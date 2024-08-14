import os

# 要添加的许可证文本
license_text = '''\
# Copyright 2024 THU-BPM MarkLLM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''

def add_license_to_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # 如果许可证已经存在，则跳过
    if license_text.strip() in content:
        return

    with open(file_path, 'w') as file:
        file.write(license_text + '\n' + content)

def add_license_to_all_py_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                add_license_to_file(file_path)
                print(f"Added license to {file_path}")

# 指定你的项目目录
project_directory = '/root/MarkLLM'
add_license_to_all_py_files(project_directory)