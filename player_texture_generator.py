import base64
import os
import json
import re
from io import BytesIO
from PIL import Image

def create_error(code, message):
    error = {
        "statusCode": 404,
        "body": json.dumps({ "error": { "code": code, "message": message }})
    }
    print(f"Returning error {error}")
    return error

def rgb_replace_color(image, box, source_color, target_color):
    region = image.crop(box)
    data = region.load()
    alpha = region.getchannel('A')

    for y in range(region.height):
        for x in range(region.width):
            if data[x, y][0] == source_color[0] and data[x, y][1] == source_color[1] and data[x, y][2] == source_color[2]:
                data[x, y] = target_color

    image.paste(region, box, mask=alpha)
    return image

def rgb_multiply_region(image, box, factors, brightness_factor = 1.0):
    """
    factors: (r_mult, g_mult, b_mult) — floats like (1.0, 0.5, 0.5)
    box: (left, upper, right, lower) — region to apply the effect
    """
    image = image.convert('RGBA')
    region = image.crop(box)

    rgb_region = region.convert('RGB')
    alpha = region.getchannel('A')

    r, g, b = rgb_region.split()
    r = r.point(lambda p: int((p * factors[0] + 30) % 256.0))
    g = g.point(lambda p: int((p * factors[1] + 30) % 256.0))
    b = b.point(lambda p: int((p * factors[2] + 30) % 256.0))

    new_region = Image.merge('RGB', (r, g, b))
    new_region.putalpha(alpha)
    image.paste(new_region, box, mask=alpha)
    return image

def lambda_handler(event, context):
    # textures_path = "release/models/players/Textures" # for debugging purposes
    textures_path = "Textures"

    ## Figure out what the user wants and do some basic validation to prevent path traversal
    query_parameters = event.get("queryStringParameters", {})

    hair_style_query = query_parameters.get("hair_style", "HAIR_1")
    if not re.fullmatch(r'[A-Za-z0-9_]+', hair_style_query):
        return create_error("invalidHairStyle", "Requested hair style does not exist")

    hair_color_query = query_parameters.get("hair_color", "HAIR_COLOR_1")
    if not re.fullmatch(r'[A-Za-z0-9_]+', hair_color_query):
        return create_error("invalidHairColor", "Requested hair color does not exist")

    skin_tone_query = query_parameters.get("skin_tone", "SKIN_TONE_3")
    if not re.fullmatch(r'[A-Za-z0-9_]+', skin_tone_query):
        return create_error("invalidSkinTone", "Requested skin tone does not exist")

    clothing_query = query_parameters.get("clothing", "CLOTHING_1")
    if not re.fullmatch(r'[A-Za-z0-9_]+', clothing_query):
        return create_error("invalidClothing", "Requested clothing does not exist")

    eye_color = query_parameters.get("eye_color", "00FF00")
    if not re.fullmatch(r'[A-Fa-f0-9]+', eye_color) or len(eye_color) != 6:
        return create_error("invalidEyeColor", "Eye color must be a valid RGB value")

    ## Parse queries
    clothing_id = clothing_query.replace("CLOTHING_", "")
    hair_style_id = hair_style_query.replace("HAIR_", "")
    hair_color_id = hair_color_query.replace("HAIR_COLOR_", "")
    skin_tone_id = skin_tone_query.replace("SKIN_TONE_", "")
    
    ## Check if the requested stuff actually exists
    clothing_path = f"{textures_path}/clothing-texture/{clothing_id}/clothing-{clothing_id}.png"
    hair_style_path = f"{textures_path}/hairstyle-texture/{hair_style_id}/hair-{hair_style_id}-{hair_color_id}.png"
    skin_tone_path = f"{textures_path}/skin-texture/skin-tone-{skin_tone_id}.png"
    
    if not os.path.exists(clothing_path):
        return create_error("invalidClothing", "Requested clothing does not exist")
    
    if not os.path.exists(hair_style_path):
        return create_error("invalidHairStyle", "Requested hair style does not exist")
    
    if not os.path.exists(skin_tone_path):
        return create_error("invalidSkinTone", "Requested skin tone does not exist")

    ## Generate the output texture
    base_img = Image.new(mode="RGBA", size=(256,256))
    eyes_img = Image.open(f"{textures_path}/eye-texture/eye-texture.png")
    pupils_img = Image.open(f"{textures_path}/eye-texture/pupil-texture.png")
    
    clothing_img = Image.open(clothing_path)
    hair_style_img = Image.open(hair_style_path)
    skin_tone_img = Image.open(skin_tone_path)

    # Generate pupil image
    eye_color_r = int(eye_color[0:2], 16)
    eye_color_g = int(eye_color[2:4], 16)
    eye_color_b = int(eye_color[4:6], 16)
    pupils_img = rgb_replace_color(pupils_img, (0, 0, 20, 20), (0, 135, 28), (eye_color_r, eye_color_g, eye_color_b, 255))

    # Overlay images on top of each other
    base_img.paste(im=clothing_img, box=(0,0), mask=clothing_img)
    base_img.paste(im=hair_style_img, box=(0,0), mask=hair_style_img)
    base_img.paste(im=skin_tone_img, box=(0,0), mask=skin_tone_img)
    base_img.paste(im=eyes_img, box=(0,0), mask=eyes_img)
    base_img.paste(im=pupils_img, box=(0,0), mask=pupils_img)

    buf = BytesIO()
    base_img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode()

    # base_img.save("out.png")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "image/png"},
        "isBase64Encoded": True,
        "body": b64
    }