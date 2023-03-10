# Copyright 2022 The KerasNLP Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

import tqdm

# Clean these folders and saved parsed version of them.
clean_folders = ["bnwiki", "arwiki", "ruwiki", "ptwiki", "idwiki"]

for clean_folder_ in clean_folders:
    clean_folder = clean_folder_
    output_folder = f"{clean_folder_}_parsed"
    os.mkdir(output_folder)
    for folder in tqdm.tqdm(os.listdir(clean_folder)):
        path = os.path.join(clean_folder, folder)
        os.mkdir(os.path.join(output_folder, folder))
        for file in os.listdir(path):
            article = []
            with open(os.path.join(path, file)) as f:
                article.extend(
                    line
                    for line in f
                    if not line.startswith("</doc>")
                    and not line.startswith("<doc")
                )
            with open(os.path.join(output_folder, folder, file), "w+") as f:
                for line in article:
                    f.write(line + "\n")
