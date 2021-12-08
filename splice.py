from PIL import Image
import random
import os, os.path

ASSETS = "./assets"
BODY = "/body"
FACE = "/face"
HEAD = "/head"

def main():

    print("Splicing...")

    collection = Image.new(mode="RGB", size=(7500, 7500), color=(255, 255, 255))

    for x in range(10):
        for y in range(10):

            # Generate random ID.
            bodyId = random.randrange(0, len(os.listdir(f"{ASSETS}{BODY}")) -1 )
            faceId = random.randrange(0, len(os.listdir(f"{ASSETS}{FACE}")) -1 )
            headId = random.randrange(0, len(os.listdir(f"{ASSETS}{HEAD}")) -1 )

            # Open Required pngs in respective folders.
            print(f"Opening body {ASSETS}{BODY}/{bodyId}.png")
            body = Image.open(f"{ASSETS}{BODY}/{bodyId}.png")

            print(f"Opening face {ASSETS}{BODY}/{faceId}.png")
            face = Image.open(f"{ASSETS}{FACE}/{faceId}.png")

            print(f"Opening head {ASSETS}{BODY}/{headId}.png")
            head = Image.open(f"{ASSETS}{HEAD}/{headId}.png")

            canvas = Image.new(mode="RGB", size=(700, 700), color=(255, 255, 255))

            # Paste/Merge Required PNGs, as layers on base
            print("Pasting images...")

            # Paste body at bottom of canvas.
            body.x = int( canvas.width / 2 - body.width/2 )
            body.y = int( canvas.height - body.height )
            canvas.paste(body, (body.x, body.y))

            # Paste head above top of body.
            head.x = int( body.x + body.width/2 - head.width/2 )
            head.y = int( body.y - head.height )
            canvas.paste(head, (head.x, head.y))

            # Paste face below top of body.
            face.x = int( body.x + body.width/2 - face.width/2 )
            face.y = int( body.y )
            canvas.paste(face, (face.x, face.y))

            # Save output
            print(f"Pasting canvas onto collection {x}, {y}...")
            collection.paste(canvas, (x * 750, y * 750))

    print(f"Saving to output...")
    collection.save(f"{ASSETS}/output.png")

if __name__ == "__main__":
    main()