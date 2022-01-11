B=True
import logging as C
from homeassistant.components.frontend import add_extra_js_url as I
from homeassistant.components.http.view import HomeAssistantView as J
import json
from os import walk,path
N=C.getLogger(__name__)
A='hass-hue-icons-integration'
O='frontend_extra_module_url'
D=f"/{A}/main.js"
K=f"custom_components/{A}/main.js"
L=f"/{A}/icons"
E=f"/{A}/list"
F=f"custom_components/{A}/data"
M=f"/{A}/icons/my"
G='my_icons/'
class H(J):
	requires_auth=False
	def __init__(A,url,iconpath):A.url=url;A.iconpath=iconpath;A.name='Icon Listing'
	async def get(A,request):
		B=[]
		for (C,E,D) in walk(A.iconpath):B.extend([{'name':path.join(C[len(A.iconpath):],B[:-4])}for B in D if B.endswith('.svg')])
		return json.dumps(B)
async def async_setup(hass,config):C='/svgs';A=hass;A.http.register_static_path(D,A.config.path(K),B);I(A,D);A.http.register_static_path(L+C,A.config.path(F+C),B);A.http.register_view(H(E+C,A.config.path(F+C)));A.http.register_static_path(M,A.config.path(G),B);A.http.register_view(H(E+'/my',A.config.path(G)));return B
async def async_setup_entry(hass,entry):return B
async def async_remove_entry(hass,entry):return B