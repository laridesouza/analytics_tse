# %%
import argparse

from downloader import DownloadTSE
from extract import ExtractFromZip

# %%

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Baixar dados do TSE")
    parser.add_argument("--inicio",'-i', type=int, help="Ano inicial a ser baixado")
    parser.add_argument("--fim", '-f', type=int, help="Ano final a ser baixado")
    parser.add_argument("--intervalo", type=int, default=2, help="Intervalo entre os anos a serem baixados")
    args = parser.parse_args()

    downloader = DownloadTSE()
    downloader.download_anos(
        range(
            args.inicio,
            args.fim + 1,
            args.intervalo))
    
    extractor = ExtractFromZip()
    extractor.extract_anos(range(args.inicio, args.fim + 1, args.intervalo))

