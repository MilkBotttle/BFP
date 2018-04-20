from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client
"""
load from env
        auth_url=os.environ["OS_AUTH_URL"],
        username=os.environ["OS_USERNAME"],
        password=os.environ["OS_PASSWORD"],
        user_domain_id=os.environ["OS_USER_DOMAIN_ID"],
        project_domain_id=os.environ["OS_PROJECT_DOMAIN_ID"],
        project_name=os.environ["OS_PROJECT_NAME"],
"""
def prepare_param(request):
    return param


def create_session(param):
    loader = loading.get_plugin_loader('password')
    #
    #print(loader.get_options())
    auth= loader.load_from_options(
        auth_url=param['auth_url']
        username=os.environ["OS_USERNAME"],
        password=os.environ["OS_PASSWORD"],
        user_domain_id=os.environ["OS_USER_DOMAIN_ID"],
        project_domain_id=os.environ["OS_PROJECT_DOMAIN_ID"],
        project_name=os.environ["OS_PROJECT_NAME"],
    )
    sess = session.Session(auth=auth) 
def novaclient(version,session):
    c = client.Client(version,session)
    return c
    


def     
