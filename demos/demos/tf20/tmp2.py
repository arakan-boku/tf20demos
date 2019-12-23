import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image as Image


class MobileNetV2:

    def __init__(self):
        self.IMAGE_SHAPE = 224
        self.classifier = tf.keras.Sequential([
            hub.KerasLayer("https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4", trainable=False),
            tf.keras.layers.Dense(3, activation='softmax')
        ])
        # Batch input shape.
        self.classifier.build([None, self.IMAGE_SHAPE, self.IMAGE_SHAPE, 3])
        # クラス名データ。結果は数字なので、これを使って英語名にする
        data_url = "https://storage.googleapis.com/download.tensorflow.org/data/"
        # 英語クラス名を取得するためのデータファイルを取得してリストに変換する
        labels_path = tf.keras.utils.get_file(
            'ImageNetLabels.txt',
            data_url + 'ImageNetLabels.txt')
        self.imagenet_labels = np.array(open(labels_path).read().splitlines())

    def predict_from_path(self, imgpath):
        # 画像データの読み込みとデータ化
        target_image = Image.open(imgpath).resize(
            (self.IMAGE_SHAPE, self.IMAGE_SHAPE))
        target_image_array = np.array(target_image) / 255.0
        # 分類予測実行
        result = self.classifier.predict(target_image_array[np.newaxis, ...])
        # 分類予測結果をとりだし、英語名に変換
        predicted_class = np.argmax(result[0], axis=-1)
        return self.imagenet_labels[predicted_class]


if __name__ == '__main__':
    m = MobileNetV2()
    a = m.predict_from_path('.\\tf20\\test.jpg')
    print(a + 'です。')
