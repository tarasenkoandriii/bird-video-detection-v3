"""Copy locally obtained LaSOT frames into the v3 YOLO directory layout."""
import argparse, json, shutil
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--lasot-root', required=True, help='Directory containing bird-5/, bird-9/, etc.')
p.add_argument('--repo', default='.', help='Root of this cloned repository')
a=p.parse_args(); root=Path(a.repo); source=Path(a.lasot_root)
index=root/'corpus_frame_index.jsonl'
for line in index.open():
    row=json.loads(line)
    src=source/row['source_member']
    dst=root/row['split']/'images'/(Path(row['image']).name)
    if not src.is_file():
        raise FileNotFoundError(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src,dst)
print('Copied full corpus images. Pilot images can be taken from matching frames in train/images and val/images.')
