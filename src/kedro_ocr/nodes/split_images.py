import cv2

def train_test_split(raw: list) -> list:
	train = raw[:2]
	test = raw[2:]
	return [train, test]