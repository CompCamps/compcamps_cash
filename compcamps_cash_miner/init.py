from compcamps_cash_api import CompCampsCashApi
from compcamps_cash_api.entities import Keys

# Initialize public/private key library
myKeys = Keys()
public_key, _ = myKeys.getEncodedKeys()
ccapi = CompCampsCashApi("http://localhost:5000") # Initalize & establish connection to CCC Server