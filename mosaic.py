''' python mosaic.py sample.jpg '''

import cv2
import numpy as np
import os
import sys
import pathlib
import datetime
import time
import platform


# 引数は画像のファイルパス
args = sys.argv[1]
src = cv2.imread(args)

ratio = 0.1
small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
big = cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

pts = np.array([[500,720],[1280,220],[1280,720]])
mask = cv2.fillConvexPoly(src, pts, (255,255,255))
img = np.where(mask == 255, big, src)

cv2.imshow("mosaic", img)
# 任意のファイルパスを指定
path = pathlib.Path(args)
st = path.stat() # pathlib.Pathオブジェクトからメタデータを取得
# stat().st_ctimeがWindowsにおけるファイルの作成日時
dt = datetime.datetime.fromtimestamp(st.st_ctime) # 得られるタイムスタンプはUNIX時間なのでdatetime型に変換
dt_fm = f"{dt:%Y%m%d_%H%M}" # ファイル名に使いやすいようにフォーマット
filepath = str(path.parent) + '/' + dt_fm + path.suffix
#filepath = str(path.parent) + '/' + path.stem + '_mosaic' + path.suffix

count = 1
if os.path.exists(filepath) == False:
    cv2.imwrite(filepath, img)
    print("Save completed. Image's filename:", filepath)
else:
    path = pathlib.Path(filepath)
    filepath = str(path.parent) + '/' + dt_fm + '_' + str(count) + path.suffix
    cv2.imwrite(filepath, img)
    print("There is already a file with the same name. Saved the file with a new name.")
    print("Image's filename: ", filepath)
    count += 1

cv2.waitKey()
cv2.destroyAllWindows()