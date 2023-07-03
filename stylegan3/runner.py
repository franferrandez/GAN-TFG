"""
Genera imagenes con los modelos de stylegan3.

IMPORTANTE: Para que funcione, hay que tener instalado ZIP desde choco: choco install zip
"""
import os

GENERAR_IMGS = 25
ZIP = True
COMMAND="docker run --gpus all -it --rm -v .\stylegan3:/scratch --workdir /scratch -e HOME=/scratch stylegan3 python gen_images.py --outdir=out --trunc=1"

modelos = {
    "gatos": {
        "link": "https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-afhqv2-512x512.pkl",
        "carpeta": "gatos"
    },
    "personas1": {
        "link": "https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan3/versions/1/files/stylegan3-r-ffhqu-256x256.pkl",
        "carpeta": "personas1"
    },
    "personas2": {
        "link": "https://api.ngc.nvidia.com/v2/models/nvidia/research/stylegan2/versions/1/files/stylegan2-celebahq-256x256.pkl",
        "carpeta": "personas2"
    },
}

if __name__ == '__main__':
    os.makedirs("zips", exist_ok=True)
    print("Bienvenido al clasificador de imagenes")
    print("Generando modelo de gatos")
    for i in range(GENERAR_IMGS):
        os.system(f"{COMMAND} --seeds={i} --network={modelos['gatos']['link']}")
    os.system(f"zip -r zips/{modelos['gatos']['carpeta']}.zip out/")

    print("Generando modelo de personas1")
    for i in range(GENERAR_IMGS):
        os.system(f"{COMMAND} --seeds={i} --network={modelos['personas1']['link']}")
    os.system(f"zip -r zips/{modelos['personas1']['carpeta']}.zip out/")

    print("Generando modelo de personas2")
    for i in range(GENERAR_IMGS):
        os.system(f"{COMMAND} --seeds={i} --network={modelos['personas2']['link']}")
    os.system(f"zip -r zips/{modelos['personas2']['carpeta']}.zip out/")
    os.system(f"zip -r general.zip zips/")
    