# main.py
import argparse
from pathlib import Path
import core2026_7_9
def main():
    parser = argparse.ArgumentParser(description='课程资料整理器')
    parser.add_argument('--source', required=True, help='原始课程资料所在目录')
    parser.add_argument('--target', required=True, help='整理后的目标目录')
    parser.add_argument('--mode', choices=['copy', 'move'], default='copy', help='操作模式：copy复制 move移动')
    parser.add_argument('--dry-run', action='store_true', help='只预览不执行')
    args = parser.parse_args()
    core2026_7_9.organize_files(
        source_dir=args.source,
        target_dir=args.target,
        mode=args.mode,
        dry_run=args.dry_run
    )
if __name__ == '__main__':
    main()