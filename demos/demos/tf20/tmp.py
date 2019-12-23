import tensorflow as tf
import numpy as np


class Vgg16k:

    def __init__(self):
        self.model = tf.keras.applications.VGG16(
            weights='imagenet', include_top=True)
        self.IMAGE_SHAPE = (224, 224)

    def __predict(self, img):
        x = tf.keras.preprocessing.image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = tf.keras.applications.vgg16.preprocess_input(x)
        features = self.model.predict(x)
        results = tf.keras.applications.vgg16.decode_predictions(features, top=1)[0]
        ans = {}
        ans['pp'] = '{:.2f}'.format(results[0][2] * 100.0) + '%'
        ans['en'] = results[0][1]
        return ans

    def predict_from_path(self, imgpath):
        img = tf.keras.preprocessing.image.load_img(
            imgpath, target_size=self.IMAGE_SHAPE)
        return self.__predict(img)


if __name__ == '__main__':
    m = Vgg16k()
    a = m.predict_from_path('.\\tf20\\test.jpg')
    print(a['en'] + 'です。確率は' + a['pp'])
