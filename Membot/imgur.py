# pylint: disable=line-too-long,import-error

"""
Module related to uploading images to imgur account.
"""

from imgurpython import ImgurClient

CLIENT_ID = 'f89b537cec2a120'
CLIENT_SECRET = 'c31647c68a98833618da773fbe566777cec81103'
REFRESH_TOKEN = '549d6c3ae49ae9d6b0b98cd1fa176b64b5180b81'

client = ImgurClient(CLIENT_ID, CLIENT_SECRET, '', REFRESH_TOKEN)


# dodaj zdjecie na platforme imgur
async def imgur_upload(file_url):
    """
    Function uploading image to an account server.
    """
    # image_path = f'attachments/{name}'
    # response = client.upload_from_path(image_path, config=None, anon=True)
    response = client.upload_from_url(url=file_url, config=None, anon=True)
    print(response)
    return response
