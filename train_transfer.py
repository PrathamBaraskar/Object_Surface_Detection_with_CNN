import os, cv2
import numpy as np 
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_path = r"C:\Users\Pratham\Desktop\Artifiical intelligence\Deep learning\projects\NEU-DET\train"
val_path = r"C:\Users\Pratham\Desktop\Artifiical intelligence\Deep learning\projects\NEU-DET\validation"

def load_images(folder):
    images, labels = [],[]
    classes = os.listdir(folder)
    classes.sort()
    for idx, cls in enumerate(classes):
        cls_folder = os.path.join(folder, cls)
        if not os.path.isdir(cls_folder):
            continue
        for img_file in os.listdir(cls_folder):
            img_path = os.path.join(cls_folder, img_file)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.resize(img, (224,224))
                images.append(img)
                labels.append(idx)
    return np.array(images)/255.0, to_categorical(labels, num_classes = len(classes)), classes 


x_train, y_train , classes = load_images(train_path)
x_val, y_val, _ = load_images(val_path)

datagen = ImageDataGenerator(
    rotation_range = 20,
    width_shift_range = 0.1,
    height_shift_range = 0.1,
    horizontal_flip = True ,
    zoom_range = 0.1
)

base_model = ResNet50(weights = 'imagenet', include_top = False, input_shape= (224,224,3))
x = GlobalAveragePooling2D()(base_model.output)
x = Dense(128, activation = 'relu')(x)
output = Dense(len(classes), activation = 'softmax')(x)
model = Model(inputs = base_model.inputs , outputs = output)

for layer in base_model.layers: #open last 10 layers 
    layer.trainable = False

early_stop = EarlyStopping(monitor = 'val_accuracy', patience = 5, restore_best_weights = True)    

model.compile(optimizer = Adam(learning_rate = 1e-6), loss = 'categorical_crossentropy', metrics = ['accuracy'])
model.fit(datagen.flow(x_train, y_train ,batch_size = 32), epochs = 10, validation_data = (x_val, y_val), callbacks = [early_stop])   

model.save('resnet_model.keras')
print('model is saved sucessfully ')