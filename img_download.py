import requests
import os
import cv2
import numpy as np
import datetime


def download_image(url, timeout=10):
    res = requests.get(url, allow_redirects=False, timeout=timeout)
    if res.status_code != 200:
        e = Exception("HTTP status: " + res.status_code)
        raise e

    content_type = res.headers["content-type"]
    if "image" not in content_type:
        e = Exception("Content-Type: " + content_type)
        raise e
    return res.content


def make_filename(base_dir, number, url):
    ext = os.path.splitext(url)[1]    # 拡張子を取得
    now = datetime.datetime.now()
    #date_now = "{0:%Y%m%d_%H%M}".format(now)    # python3.5以前用
    date_now = f"{now:%Y%m%d_%H%M}"
    filename = date_now + ext    # 現在時刻 + 拡張子がファイル名
    fullpath = os.path.join(base_dir, filename)
    if os.path.exists(fullpath) == True:
        filename = date_now + str(number) + ext    # 現在時刻 + 番号 + 拡張子がファイル名
        fullpath = os.path.join(base_dir, filename)
    return filename, fullpath    # filenameはmosaic保存時、fullpathはOpenCV画像読み込み時に使う


def save_image(filename, image):
    with open(filename, "wb") as fout:
        fout.write(image)


def mosaic_img(base_dir, filename, filepath):
    src = cv2.imread(filepath)
    ratio = 0.1
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    big = cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    pts = np.array([[500, 720], [1280, 220], [1280, 720]])    # mosaicかける部分、適宜変更可
    mask = cv2.fillConvexPoly(src, pts, (255, 255, 255))
    img = np.where(mask == 255, big, src)
    fullpath = os.path.join(base_dir, filename)
    cv2.imwrite(fullpath, img)
    #cv2.imshow("mosaic", img)
    #cv2.waitKey()
    #cv2.destroyAllWindows()


if __name__ == '__main__':
    url_txt = "url_list.txt"    # .jpgなどで終わるURLが入力されたtxtファイル
    images_dir = "picture"    # pictureディレクトリが必要
    mosaic_dir = "mosaics"    # mosaicsが必要。これらは作業ディレクトリ内に作成
    idx = 0
    with open(url_txt, "r") as fin:    # "r"は読み込み専用
        for line in fin:
            url = line.strip()
            filename, filepath = make_filename(images_dir, idx, url)
            print("%s" % url)
            try:
                image = download_image(url)
                save_image(filepath, image)
                idx += 1
                mosaic_img(mosaic_dir, filename, filepath)
            except KeyboardInterrupt:
                break
            except Exception as err:
                print("%s" % err)