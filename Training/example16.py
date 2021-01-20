import cv2
import numpy as np
import glob

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cells = [np.hsplit(row, 100) for row in np.vsplit(gra, 50)]
x = np.array(cells)

train = x[:, :].reshape(-1, 400).astype(np.float32)

k = np.arange(10)
train_labels = np.repeat(k, 500)[:, np.newaxis]

np.save2('trained.npz', train = train, train_labels = train_labels)

# KNN 숫자 인식하기
FILE_NAME = 'trained.npz'

# 파일로부터 학습 데이터 불러오기
def load_train_data(file_name) :
    with np.load(file_name) as data:
        train = data['train']
        train_labels = data['train_labels']
    return train, train_labels

# 손 글씨 이미지를 (20 X 20) 크기로 Scaling한다.
def resize20(image) :
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_resize = cv2.resize(gra, (20, 20))
    plt.imshow(cv2.cvtColor(gray_resize, cv2.COLOR_GRAY2RGB))
    plt.show()

    # 최종적으로 (1 X 400) 크기로 반환한다.
    return gray_resize.reshape(-1, 400).astype(np.float32)

def check(test, train, train_labels):
    knn = cv2.ml.KNearest_create()
    knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

    # 가장 가까운 5개의 글잘르 찾고, 어떤 숫자에 해당하는지 찾는다.
    ret, result, neighbours, dist = knn.findNearest(test, k = 5)
    return result

train, train_labels = load_train_data(FILE_NAME)

for file_name in glob.glob('./test_+.png'):
    test = resize20(file_name)
    result = check(test, train, train_labels)
    print(result)
