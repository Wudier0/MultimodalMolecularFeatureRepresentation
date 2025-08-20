import os
import requests
from tqdm import tqdm

# AlphaFold PDB 文件的 URL 模板
AF_URL_TEMPLATE = "https://alphafold.ebi.ac.uk/files/AF-{protein_id}-F1-model_v4.pdb"

# 读取蛋白质 ID 列表
def read_protein_ids(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

# 下载单个 PDB 文件
def download_pdb(protein_id, output_dir):
    url = AF_URL_TEMPLATE.format(protein_id=protein_id)
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        file_path = os.path.join(output_dir, f"{protein_id}.pdb")
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return True
    else:
        print(f"Failed to download {protein_id}: HTTP {response.status_code}")
        return False

# 批量下载 PDB 文件
def batch_download_pdb(protein_ids, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    success_count = 0
    for protein_id in tqdm(protein_ids, desc="Downloading PDB files"):
        if download_pdb(protein_id, output_dir):
            success_count += 1
    
    print(f"Download completed: {success_count}/{len(protein_ids)} files downloaded.")

# 主函数
if __name__ == "__main__":
    # 蛋白质 ID 列表文件路径
    protein_id_file = "protein_ids.txt"
    # 输出目录
    output_dir = "data/Davis/PDB_AF2/"
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取蛋白质 ID 列表
    protein_ids = read_protein_ids(protein_id_file)
    print(f"Loaded {len(protein_ids)} protein IDs.")
    
    # 批量下载 PDB 文件
    batch_download_pdb(protein_ids, output_dir)