from projectpkg.auth.signup import signuplib
from projectpkg.auth.login import loginlib
from projectpkg.user import userdata

signuplib.usersignup("riddhi","vekariya","riddhi12","riddhi@12")

loginlib.userlogin("admin","admin")

userdata.newuser(101,'riddhi','Rajkot')