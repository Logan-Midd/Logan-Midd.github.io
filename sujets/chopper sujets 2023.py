import requests
import os
import threading
import time

annees_sites = (
    ("2023", "https://pixees.fr/informatiquelycee/term/ep/2023", 45),
    ("2024", "https://pixees.fr/informatiquelycee/term/ep/courant", 48)
)

def check_for_404(url):
    r = requests.get(url)
    if r.status_code != 404:
        return r
    print(f"404: {url}")


def trouver_sujet_pdf(numero, path, base_url):
    r = check_for_404(f"{base_url}/{numero}.pdf")
    with open(f"{path}/sujet_{numero}.pdf", "wb+") as f:
        f.write(r.content)


def trouver_sujet_py(numero, path, base_url):
    r = check_for_404(f"{base_url}/{numero}.py")
    with open(f"{path}/sujet_{numero}_py.py", "w+", encoding="utf-16") as f:
        f.write(r.text)


def trouver_correction_sujet_1(numero, path, base_url):
    r = check_for_404(f"{base_url}/c{numero}_01.py")
    with open(f"{path}/sujet_{numero}_correction_1.py", "w+", encoding="utf-16") as f:
        f.write(r.text)


def trouver_correction_sujet_2(numero, path, base_url):
    r = check_for_404(f"{base_url}/c{numero}_02.py")
    with open(f"{path}/sujet_{numero}_correction_2.py", "w+", encoding="utf-16") as f:
        f.write(r.text)


def main():

    for annee, base_url, num_sujets in annees_sites:
        start = time.perf_counter()

        threads = []

        os.mkdir(f"./sujets_{annee}")

        for i in range(1, num_sujets + 1):
            numero = str(i) if i > 9 else "0" + str(i)
            path = f"./sujets_{annee}/sujet_{i}"
            os.mkdir(path)
            t_correction_1 = threading.Thread(target=lambda num=numero, file_path=path: trouver_correction_sujet_1(num, file_path, base_url), daemon=True)
            t_correction_2 = threading.Thread(target=lambda num=numero, file_path=path: trouver_correction_sujet_2(num, file_path, base_url), daemon=True)
            t_sujet_py = threading.Thread(target=lambda num=numero, file_path=path: trouver_sujet_py(num, file_path, base_url), daemon=True)
            t_sujet_pdf = threading.Thread(target=lambda num=numero, file_path=path: trouver_sujet_pdf(num, file_path, base_url), daemon=True)
            threads.append((t_sujet_pdf, t_sujet_py, t_correction_1, t_correction_2))

        for thread_tuple in threads:
            for thread in thread_tuple:
                thread.start()

        for thread_tuple in threads:
            for thread in thread_tuple:
                thread.join()

        end = time.perf_counter()
        print(f"Contenu de {annee} téléchargé en {round(end - start, 3)} secondes")




if __name__ == "__main__":
    main()
