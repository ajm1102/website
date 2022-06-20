import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from serverConfig import ACCESS_ID, SECRET_KEY

def plotcord(Xcords, Ycords):
    plt.scatter(Xcords, Ycords)
    img = None
    return img


def upload_spaces(x, y):
    from boto3 import session
    from botocore.client import Config

    x = x.split(',')
    y = y.split(',')

    plt.scatter(x, y)


    # Initiate session
    session = session.Session()
    client = session.client('s3',
                            region_name='nyc3',
                            endpoint_url='https://spaceaidan.fra1.digitaloceanspaces.com',
                            aws_access_key_id=ACCESS_ID,
                            aws_secret_access_key=SECRET_KEY)

    # Upload a file to your Space
    name = 'figure1.png'

    plt.savefig(name)
    plt.close()
    client.upload_file('figure1.png', 'hello-spaces', f'new-folder/{name}', ExtraArgs={'ACL':'public-read'})
    os.remove('figure1.png')
    return
