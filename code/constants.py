DATA_FOLDER = './data'
TEST_FOLDER = DATA_FOLDER + '/' + 'test'   	# folder with testing images
TRAIN_FOLDER = DATA_FOLDER + '/' + 'train' 	# folder with training images

MODEL_FOLDER = './model'

RESULT_FOLDER = './result'

IMAGE_HEIGHT = 77  # height of the image
IMAGE_WIDTH = 71   # width of the image
NUM_CHANNELS = 1   # number of channels of the image
NUM_IMAGES = -1    # number of train images

SPLIT_RATE = 0.75	# split rate for training and validation sets

LEARNING_RATES = [0.001, 0.00055, 0.0001]
NUM_EPOCHS_LIMIT = 20

BATCH_SIZE = 64