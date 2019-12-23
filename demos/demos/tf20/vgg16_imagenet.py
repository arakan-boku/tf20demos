import tensorflow as tf
import numpy as np
import PIL.Image as Image
from io import BytesIO
import base64
from . import to_japanese_ilsvrc2012 as toj


class Vgg16k:

    def __init__(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            weights='imagenet', include_top=True)
        self.translator = toj.Ilsvrc2012Japanese()
        self.IMAGE_SHAPE = (224, 224)

    def __predict(self, img):
        x = tf.keras.preprocessing.image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = tf.keras.applications.vgg16.preprocess_input(x)
        pred = self.model.predict(x)
        results = tf.keras.applications.vgg16.decode_predictions(pred, top=1)[
            0]
        ans = {}
        ans['pp'] = '{:.2f}'.format(results[0][2] * 100.0) + '%'
        ans['jp'] = self.translator.convert(results[0][1])
        ans['en'] = results[0][1]
        return ans

    def predict_from_path(self, imgpath):
        img = tf.keras.preprocessing.image.load_img(
            imgpath, target_size=self.IMAGE_SHAPE)
        return self.__predict(img)

    def predict_from_base64(self, base64text):
        img = Image.open(
            BytesIO(
                base64.b64decode(base64text))).resize(
            self.IMAGE_SHAPE)
        return self.__predict(img)


if __name__ == '__main__':
    def base64encode(file_name):
        target_file = file_name
        with open(target_file, 'rb') as f:
            data = f.read()
        encoded_base64_text = base64.b64encode(data)
        return encoded_base64_text

    m = Vgg16k()
    a = m.predict_from_base64(base64encode('.\\tf20\\test.jpg'))
    print(a['jp'])
