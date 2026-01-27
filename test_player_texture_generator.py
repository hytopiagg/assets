import player_texture_generator

def test_player_texture_generator():
    result = player_texture_generator.lambda_handler({
        "queryStringParameters": {
            "hair_style": "HAIR_1",
            "hair_color": "HAIR_COLOR_1",
            "skin_tone": "SKIN_TONE_1",
            "clothing": "CLOTHING_1",
            "eye_color": "FF00FF"
        }
    }, {})
    print(result)

test_player_texture_generator()