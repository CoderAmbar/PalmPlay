import cv2
import mediapipe as mp
from pynput.keyboard import Controller

keyboard = Controller()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def is_hand_open(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]
    fingers_up = 0
    for tip_id in tips_ids:
        tip = hand_landmarks.landmark[tip_id]
        pip = hand_landmarks.landmark[tip_id - 2]
        if tip.y < pip.y:
            fingers_up += 1
    return fingers_up >= 4

pressed_keys = set()

def press_key(key):
    if key not in pressed_keys:
        keyboard.press(key)
        pressed_keys.add(key)

def release_key(key):
    if key in pressed_keys:
        keyboard.release(key)
        pressed_keys.remove(key)

def release_all():
    for key in list(pressed_keys):
        release_key(key)

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    left_hand_open = False
    right_hand_open = False

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, handLms in enumerate(results.multi_hand_landmarks):
            hand_label = results.multi_handedness[idx].classification[0].label
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            if is_hand_open(handLms):
                if hand_label == 'Left':
                    left_hand_open = True
                elif hand_label == 'Right':
                    right_hand_open = True

        # Decision Logic — only when hands are visible
        if left_hand_open and right_hand_open:
            press_key('w')
            release_key('a')
            release_key('d')
            release_key('s')
        elif not left_hand_open and not right_hand_open:
            press_key('s')
            release_key('w')
            release_key('a')
            release_key('d')
        elif left_hand_open and not right_hand_open:
            press_key('w')
            press_key('a')
            release_key('s')
            release_key('d')
        elif right_hand_open and not left_hand_open:
            press_key('w')
            press_key('d')
            release_key('s')
            release_key('a')
    else:
        release_all()

    cv2.imshow("Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

release_all()
cap.release()
cv2.destroyAllWindows()
