from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


def build_pdf(images_dir: Path, output: Path) -> None:
    images = sorted(
        [p for p in images_dir.iterdir() if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'}]
    )
    if not images:
        raise RuntimeError(f'Aucune image trouvée dans {images_dir}')

    output.parent.mkdir(parents=True, exist_ok=True)
    first = Image.open(images[0])
    width, height = first.size
    pdf = canvas.Canvas(str(output), pagesize=(width, height))

    for image_path in images:
        with Image.open(image_path) as img:
            w, h = img.size
        pdf.setPageSize((w, h))
        pdf.drawImage(ImageReader(str(image_path)), 0, 0, width=w, height=h, preserveAspectRatio=True, mask='auto')
        pdf.showPage()

    pdf.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--images-dir', default='output/pages')
    parser.add_argument('--output', default='output/Regards_au_Levant.pdf')
    args = parser.parse_args()
    build_pdf(Path(args.images_dir), Path(args.output))
