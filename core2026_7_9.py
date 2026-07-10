# core.py
import shutil
from collections import defaultdict
from pathlib import Path
from datetime import datetime
from rule2026_7_9 import HOMEWORK_KEYWORDS, EXTENSION_RULES
def get_category(filename):
    name = Path(filename).stem
    ext = Path(filename).suffix.lower()
    for keyword in HOMEWORK_KEYWORDS:
        if keyword in name:
            return 'homework'
    for category, extensions in EXTENSION_RULES.items():
        if ext in extensions:
            return category
    return 'others'
def get_unique_path(target_dir, filename):
    target_path = target_dir / filename
    if not target_path.exists():
        return target_path
    stem = Path(filename).stem
    ext = Path(filename).suffix
    counter = 1
    while True:
        new_name = f"{stem}_{counter}{ext}"
        new_path = target_dir / new_name
        if not new_path.exists():
            return new_path
        counter += 1
def organize_files(source_dir, target_dir, mode='copy', dry_run=False):
    source = Path(source_dir)
    target = Path(target_dir)
    if not source.exists() or not source.is_dir():
        print(f"错误：源目录 {source} 不存在")
        return False
    report_lines = []
    report_lines.append(f"整理时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"源目录：{source.resolve()}")
    report_lines.append(f"目标目录：{target.resolve()}")
    report_lines.append(f"操作模式：{'复制' if mode == 'copy' else '移动'}")
    report_lines.append(f"运行模式：{'干跑' if dry_run else '实际执行'}")
    report_lines.append("-" * 50)
    stats = defaultdict(int)
    for item in source.iterdir():
        if not item.is_file():
            continue
        category = get_category(item.name)
        dest_dir = target / category
        dest_file = get_unique_path(dest_dir, item.name)

        stats[category] += 1

        if dry_run:
            report_lines.append(f"[预览] {item.name} -> {category}/{dest_file.name}")
        else:
            dest_dir.mkdir(parents=True, exist_ok=True)
            if mode == 'copy':
                shutil.copy2(item, dest_file)
            else:
                shutil.move(str(item), str(dest_file))
            report_lines.append(f"[完成] {item.name} -> {category}/{dest_file.name}")
    report_lines.append("-" * 50)
    report_lines.append("统计汇总：")
    total = sum(stats.values())
    for cat, count in sorted(stats.items()):
        report_lines.append(f"  {cat}: {count} 个文件")
    report_lines.append(f"  总计: {total} 个文件")
    report_text = "\n".join(report_lines)
    print(report_text)
    if not dry_run:
        target.mkdir(parents=True, exist_ok=True)
        report_path = target / "整理报告.txt"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"\n整理报告已保存至：{report_path}")
    return True