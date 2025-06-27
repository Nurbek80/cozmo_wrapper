#!/usr/bin/env python

from temporary import CozmoEasy

if __name__ == "__main__":
    cozmo = CozmoEasy()
    cozmo.say("Hello!")
    cozmo.hand_up()
    cozmo.angry()
#    cozmo.sad()
#    cozmo.happy()
#    cozmo.surprised()
#    cozmo.disgusted()


'''
with pycozmo.connect() as cli:

    # Raise head.
    angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
    cli.set_head_angle(angle)
    time.sleep(1)

    # Load image
    im = Image.open(os.path.join(os.path.dirname(__file__), "pycozmo.png"))
    # Convert to binary image.
    im = im.convert('1')

    cli.display_image(im, 10.0)

'''
'''
def main():
    with pycozmo.connect() as cli:
        face = ProceduralFace()
        face.expression = "happy"  # "happy", "neutral", "angry", etc.
        face.blink_rate = 0.5      # Blinks per second

        for _ in range(100):
            img = face.render()
            cli.display_image(img)
            time.sleep(1.0 / 20.0)  # 20 FPS

if __name__ == "__main__":
    main()'''